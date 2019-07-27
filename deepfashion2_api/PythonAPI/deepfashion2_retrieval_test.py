import json
import numpy as np
from pycocotools import mask as maskUtils


thresh = 0.5

# load retrieval results
results_image_id_all = []
results_query_score_all = []
results_query_cls_all = []
results_query_box_all = []
results_gallery_id_all = []
results_gallery_box_all = []
results_name = ' '

with open(results_name, 'r') as f:
    results = json.loads(f.read())
    for i in results:
        box = i['query_bbox']
        query_box = [box[0],box[1],box[2]-box[0],box[3]-box[1]]
        box = np.array(i['gallery_bbox'])
        gallery_box = [box[:,0], box[:,1], box[:,2] - box[:,0], box[:,3] - box[:,1]]
        gallery_box = np.transpose(gallery_box,(1,0)).tolist()
        
        results_image_id_all.append(i['query_image_id'])
        results_query_score_all.append(i['query_score'])
        results_query_cls_all.append(i['query_cls'])
        results_query_box_all.append(query_box)
        results_gallery_id_all.append(i['gallery_image_id'])
        results_gallery_box_all.append(gellery_box)
f.close()

results_image_id_all = np.array(results_image_id_all)
results_query_score_all = np.array(results_query_score_all)
results_query_cls_all = np.array(results_query_cls_all)
results_query_box_all = np.array(results_query_box_all)
results_gallery_id_all = np.array(results_gallery_id_all)
results_gallery_box_all = np.array(results_gallery_box_all)


# load query ground truth
query_image_id_all = []
query_box_all = []
query_cls_all = []
query_style_all = []
query_pair_all = []

query_name = '.../query_gt.json'
with open(query_name, 'r') as f:
    query = json.loads(f.read())
    for i in query:
        box = i['bbox']
        box = [box[0], box[1], box[2] - box[0], box[3] - box[1]]
        query_image_id_all.append(i['query_image_id'])
        query_box_all.append(box)
        query_cls_all.append(i['cls'])
        query_style_all.append(i['style'])
        query_pair_all.append(i['pair_id'])

f.close()

# load gallery ground truth
query_image_id_all = np.array(query_image_id_all)
query_box_all = np.array(query_box_all)
query_cls_all = np.array(query_cls_all)
query_style_all = np.array(query_style_all)
query_pair_all = np.array(query_pair_all)

query_num = len(np.where(query_style_all>0)[0]) # the number of all query clothing items
query_id_real= np.unique(query_image_id_all)  # image ids of query clothing items

gallery_image_id_all = []
gallery_box_all = []
gallery_style_all = []
gallery_pair_all = []

gallery_name = '.../gallery_gt.json'
with open(gallery_name, 'r') as f:
    gallery = json.loads(f.read())
    for i in gallery:
        box = i['bbox']
        box = [box[0], box[1], box[2] - box[0], box[3] - box[1]]
        gallery_image_id_all.append(i['gallery_image_id'])
        gallery_box_all.append(box)
        gallery_style_all.append(i['style'])
        gallery_pair_all.append(i['pair_id'])
f.close()

gallery_image_id_all = np.array(gallery_image_id_all)
gallery_box_all = np.array(gallery_box_all)
gallery_style_all = np.array(gallery_style_all)
gallery_pair_all = np.array(gallery_pair_all)


correct_num_1 = 0
correct_num_5 = 0
correct_num_10 = 0
correct_num_15 = 0
correct_num_20 = 0

miss_num = 0 # the number of query items that fail to be detected

for id in query_id_real:
    results_id_ind = np.where(results_image_id_all==id)[0]
    if len(results_id_ind) == 0: # in case no clothing item is detected 
        continue
    query_id_ind = np.where(query_image_id_all==id)[0] # all query items in the given image
    pair_id = query_pair_all[query_id_ind]
    assert len(np.unique(pair_id)) == 1
    pair_id = pair_id[0]

    results_id_score = results_query_score_all[results_id_ind]
    results_id_box = results_query_box_all[results_id_ind]
    results_id_cls = results_query_cls_all[results_id_ind]
    results_id_gallery_id = results_gallery_id_all[results_id_ind]
    results_id_gallery_box = results_gallery_box_all[results_id_ind]

    query_id_box = query_box_all[query_id_ind]
    query_id_cls = query_cls_all[query_id_ind]
    query_id_style = query_style_all[query_id_ind]

    is_crowd = np.zeros(len(query_id_box))
    iou_id = maskUtils.iou(results_id_box,query_id_box,is_crowd)
    iou_ind = np.argmax(iou_id,axis=1) # assign a ground truth label to each detected clothing item

    for id_ind in range(0,len(query_id_ind)):
        style = query_id_style[id_ind]
        cls = query_id_cls[id_ind]
        # For a given ground truth query item, select a detected item on behalf of it:
        # First find out all detected items which are assigned the given ground truth label 
        # and are classified correctly.
        # Then select the detected item with the highest score among these detected items.
        if style>0:
            results_style_ind1 = np.where(iou_ind==id_ind)[0]
            results_style_ind2 = np.where(results_id_cls==cls)[0]
            results_style_ind = np.intersect1d(results_style_ind1,results_style_ind2)
            if len(results_style_ind)>0:
                results_score_style = results_id_score[results_style_ind]
                score_max_ind = np.argmax(results_score_style)
                results_style_query_ind = results_style_ind[score_max_ind]
                results_style_gallery_id = results_id_gallery_id[results_style_query_ind]
                results_style_gallery_box = results_id_gallery_box[results_style_query_ind]

                # find out the corresponding ground truth items in the gallery, that is ground truth items which have the same pair id and style as the query item.
                gt_gallery_ind1 = np.where(gallery_pair_all==pair_id)[0]
                gt_gellery_ind2 = np.where(gallery_style_all==style)[0]
                gt_gallery_ind = np.intersect1d(gt_gallery_ind1,gt_gellery_ind2)
                gt_gallery_image_id = gallery_image_id_all[gt_gallery_ind]
                gt_gallery_box = gallery_box_all[gt_gallery_ind]

                assert len(gt_gallery_ind)>0

                if len(gt_gallery_ind) == 1:
                    gt_gallery_image_id = [gt_gallery_image_id]

                #calculate top-1
                for t in range(0,1):
                    # if corresponding ground truth gallery images contains retrieved gallery image,
                    # first find out the exact corresponding ground truth gallery image,
                    # then find out ground truth gallery items in this ground truth gallery image(whose number may be greater than 1)
                    # if the overlap between the retrieved gallery item and one of the ground truth gallery items is over the thresh,  the retrieved result is positive.
                    if results_style_gallery_id[t] in gt_gallery_image_id:
                        which_ind = np.where(gt_gallery_image_id==results_style_gallery_id[t])[0]
                        crowd = np.zeros(len(which_ind))
                        iou_style = maskUtils.iou([results_style_gallery_box[t]],gt_gallery_box[which_ind],crowd)
                        if len(np.where(iou_style>=thresh)[0])>0:
                            correct_num_1 = correct_num_1 + 1
                            break

                # calculate top-5
                for t in range(0,5):
                    if results_style_gallery_id[t] in gt_gallery_image_id:
                        which_ind = np.where(gt_gallery_image_id==results_style_gallery_id[t])[0]
                        crowd = np.zeros(len(which_ind))
                        iou_style = maskUtils.iou([results_style_gallery_box[t]],gt_gallery_box[which_ind],crowd)
                        if len(np.where(iou_style >= thresh)[0]) > 0:
                            correct_num_5 = correct_num_5 + 1
                            break

                # calculate top-10
                for t in range(0,10):
                    if results_style_gallery_id[t] in gt_gallery_image_id:
                        which_ind = np.where(gt_gallery_image_id==results_style_gallery_id[t])[0]
                        crowd = np.zeros(len(which_ind))
                        iou_style = maskUtils.iou([results_style_gallery_box[t]],gt_gallery_box[which_ind],crowd)
                        if len(np.where(iou_style >= thresh)[0]) > 0:
                            correct_num_10 = correct_num_10 + 1
                            break

                # calculate top-15
                for t in range(0,15):
                    if results_style_gallery_id[t] in gt_gallery_image_id:
                        which_ind = np.where(gt_gallery_image_id==results_style_gallery_id[t])[0]
                        crowd = np.zeros(len(which_ind))
                        iou_style = maskUtils.iou([results_style_gallery_box[t]],gt_gallery_box[which_ind],crowd)
                        if len(np.where(iou_style >= thresh)[0]) > 0:
                            correct_num_15 = correct_num_15 + 1
                            break

                # calculate top-20
                for t in range(0,20):
                    if results_style_gallery_id[t] in gt_gallery_image_id:
                        which_ind = np.where(gt_gallery_image_id==results_style_gallery_id[t])[0]
                        crowd = np.zeros(len(which_ind))
                        iou_style = maskUtils.iou([results_style_gallery_box[t]],gt_gallery_box[which_ind],crowd)
                        if len(np.where(iou_style >= thresh)[0]) > 0:
                            correct_num_20 = correct_num_20 + 1
                            break

            else:
                miss_num = miss_num + 1
print 'top-1'
print float(correct_num_1)/ query_num
print 'top-5'
print float(correct_num_5)/ query_num
print 'top-10'
print float(correct_num_10)/ query_num
print 'top-15'
print float(correct_num_15)/ query_num
print 'top-20'
print float(correct_num_20)/ query_num



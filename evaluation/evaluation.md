# Evaluation Overview
Evaluation metrics are introduced in [README.md](https://github.com/switchablenorms/DeepFashion2/blob/master/README.md).\
To be more specific, for clothes detection task and clothes segmentation task, evaluation metrics are the same as those introduced 
in [cocodataset](http://cocodataset.org/#home). For landmark estimation task, different from coco dataset where only one category has keypoints, a total of 294 landmarks on 13 categories are defined. Besides the coordinates of 294 landmarks of a detected clothing item, its category should also be included in the results for evaluation. Please note that after the category of a detected clothing item is predicted, only predicted landmarks pretaining to this category will actually be evaluated instead of all the 294 landmarks.(For example, if a detected clothing item is predicted as trousers, evaluation will be done between predicted landmarks and groundtruth landmarks. For trousers,the 169th to 182th landmarks of all 294 groundtruth landmarks are non-zero, thus only the 169th to 182th predicted landmarks will be evaluated.)\
For clothes retrieval task, we provide a more realistic setting for evaluation: Instead of being provided the ground truth query clothing item, you should detect clothing items in images from consumers. For each detected clothing item, you need to submit the top-20 retrieved clothing items detected from shop images. When evaluation,for each ground truth query item(whose style is greater than 0), we will select a detected item on behalf of it for retrieval: First, a ground truth label will be assigned to each detected query clothing item according to its IoU with all the ground truth items. Then find out all detected items which are assigned the given ground truth label and are classified correctly. Finally select the detected item with the highest score among these detected items. The retrieved results of this selected query item will be evaluated. If IoU between retrieved item from shop images and one of the ground truth corresponding gallery item is over the thresh(we set thresh as 0.5), the retrieved result is positive.(If none detected item is assigned the given query item label, this query item is counted as missed. )

# Evaluation Code
In [deepfashion2_api](https://github.com/switchablenorms/DeepFashion2/tree/master/deepfashion2_api), we provide evaluation code
For Python, which is based on [cocoapi](https://github.com/cocodataset/cocoapi).\
To evaluate clothes detection task, landmark estimation task or clothes segmentation task, run [deepfashion2_test.py](https://github.com/switchablenorms/DeepFashion2/blob/master/deepfashion2_api/PythonAPI/deepfashion2_test.py). To evaluate
clothes retrieval task, run [deepfashion2_retrieval_test.py](https://github.com/switchablenorms/DeepFashion2/blob/master/deepfashion2_api/PythonAPI/deepfashion2_retrieval_test.py).\
\
To install:\
Run "make" under deepfashion2_api/PythonAPI
# Ground Truth Format
In [README.md](https://github.com/switchablenorms/DeepFashion2/blob/master/README.md), we show data organization including 
images and annotations. For clothes detection task, landmark estimation task or clothes segmentation task, these annotations need to be transformed to coco-types annotation, which is defined in [cocodataset](
http://cocodataset.org/#format-data), in order to run [deepfashion2_api](https://github.com/switchablenorms/DeepFashion2/tree/master/deepfashion2_api). \
For landmark estimation task, we provide keypoints_val_vis.json and keypoints_val_vis_and_occ.json. For clothes detection and clothes segmentation task, you can generate coco-types annotation given [deepfashion2_to_coco.py](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/deepfashion2_to_coco.py).\
For clothes retrieval task, we provide val_query.json and val_gallery.json. Data structure is defined as below:
>[{
>>"gallery_image_id" : int,\
>>"style" : int,\
>>"pair_id" : int,\
>>"bbox" : [x1,y1,x2,y2],


>}]

>[{
>>"query_image_id" : int,\
>>"style" : int,\
>>"cls" : int,\
>>"pair_id" : int,\
>>"bbox" : [x1,y1,x2,y2],


>}]

# Result Format
## Clothes Detection
For detection with bounding boxes, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"bbox" : [x,y,width,height],\
>>"score" : float,

>}]

Note: box coordinates are floats measured from the top left image corner (and are 0-indexed).\
Example result JSON files are available in [example_bbox_results.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/example/example_bbox_results.json)

## Landmark Estimation
For landmark estimation, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"keypoints" : [x1,y1,v1,...,xk,yk,vk],\
>>"score" : float,

>}]

Note: keypoint coordinates are floats measured from the top left image corner (and are 0-indexed).Note also that the visibility flags vi are not currently used (except for controlling visualization), we recommend simply setting vi=1.\
Example result JSON files are available in [example_keys_results.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/example/example_keys_results.json)



## Clothes Segmentation
For segmentation, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"segmentation" : RLE,\
>>"score" : float,

>}]

Note: a binary mask containing an object segment should be encoded to RLE using the MaskApi function encode(). For additional details see [mask.py](https://github.com/switchablenorms/DeepFashion2/blob/master/deepfashion2_api/PythonAPI/pycocotools/mask.py). \
Example result JSON files are available in [example_segm_results.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/example/example_segm_results.json)


## Clothes Retrieval
For clothes retrieval, please use the following format:
>[{
>>"query_image_id" : int,\
>>"query_bbox" : [x1,y1,x2,y2],\
>>"query_cls" : int,\
>>"query_score" : float,\
>>"gallery_image_id" : [int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int],\
>>"gallery_bbox":[ [x1,y1,x2,y2],...[] ]

>}]

Note: For a detected clothing item from consumers, the top-20 retrieved clothing items from shops should be included in the 
results.\
Example result JSON files are available in [example_retrieval_results.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/example/example_retrieval_results.json)


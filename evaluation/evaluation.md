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
images and annotations. For clothes detection task, landmark estimation task or clothes segmentation task, these annotations need to be transformed to coco annotation types, which is defined in [cocodataset](
http://cocodataset.org/#format-data), in order to run [deepfashion2_api](https://github.com/switchablenorms/DeepFashion2/tree/master/deepfashion2_api). \
We will provide code to generate coco-type annotations.\
For clothes retrieval task, we provide [gallery_gt.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/gallery_gt.json) and [query_gt.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/query_gt.json). Data structure is defined as below:
>[{
>>"gallery_image_id" : int,\
>>"style" : int,\
>>"pair_id" : int,\
>>"bbox" : [x1,y1,x2,y2],


>}]\

>[{
>>"query_image_id" : int,\
>>"style" : int,\
>>"pair_id" : int,\
>>"bbox" : [x1,y1,x2,y2],


>}]\

# Result Format
## Clothes Detection
For detection with bounding boxes, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"bbox" : [x,y,width,height],\
>>"score" : float,

>}]\
Note: box coordinates are floats measured from the top left image corner (and are 0-indexed).\
Example result JSON files are available in [example_bbox_results.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/example/example_bbox_results.json)

## Landmark Estimation
For landmark estimation, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"keypoints" : [x1,y1,v1,...,xk,yk,vk],
>>"score" : float,

>}]\
Note: keypoint coordinates are floats measured from the top left image corner (and are 0-indexed).Note also that the visibility flags vi are not currently used (except for controlling visualization), we recommend simply setting vi=1.\
Example result JSON files are available in [example_keys_results.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/example/example_keys_results.json)



## Clothes Segmentation
For segmentation, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"segmentation" : RLE,\
>>"score" : float,

>}]\
Note: a binary mask containing an object segment should be encoded to RLE using the MaskApi function encode(). For additional details see [mask.py](https://github.com/switchablenorms/DeepFashion2/blob/master/deepfashion2_api/PythonAPI/pycocotools/mask.py). \
Example result JSON files are available in [example_segm_results.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/example/example_segm_results.json)


## Clothes Retrieval
For clothes retrieval, please use the following format:
>[{
>>"query_image_id" : int,\
>>"query_bbox" : [x1,y1,x2,y2],\
>>"query_score" : float,\
>>"gallery_image_id" : [int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int],\
>>"gallery_bbox":[ [x1,y1,x2,y2],...[] ]

>}]\
Note: For a detected clothing item from consumers, the top-20 retrieved clothing items from shops should be included in the 
results.\
Example result JSON files are available in [example_retrieval_results.json](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/example/example_retrieval_results.json)


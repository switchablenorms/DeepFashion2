# Evaluation Code
In [deepfashion2_api](https://github.com/switchablenorms/DeepFashion2/tree/master/deepfashion2_api), we provide evaluation code
For Python, which is based on [cocoapi](https://github.com/cocodataset/cocoapi).\
To evaluate clothes detection task, landmark estimation task or clothes segmentation task, run [deepfashion2_test.py](https://github.com/switchablenorms/DeepFashion2/blob/master/deepfashion2_api/PythonAPI/deepfashion2_test.py). To evaluate
clothes retrieval task, run [deepfashion2_retrieval_test.py](https://github.com/switchablenorms/DeepFashion2/blob/master/deepfashion2_api/PythonAPI/deepfashion2_retrieval_test.py).\
\
To install:\
Run "make" under deepfashion2_api/PythonAPI
# Ground Truth Format
In [README.md](https://github.com/switchablenorms/DeepFashion2/blob/master/README.md), we provide data organization including 
images and annotations. These annotations need to be transformed to coco annotation types, which is defined in [cocodataset](
http://cocodataset.org/#format-data), in order to run [deepfashion2_api](https://github.com/switchablenorms/DeepFashion2/tree/master/deepfashion2_api).
# Result Format
## Clothes Detection
For detection with bounding boxes, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"bbox" : [x,y,width,height],\
>>"score" : float,

>}]

## Landmark Estimation
For landmark estimation, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"keypoints" : [x1,y1,v1,...,xk,yk,vk],
>>"score" : float,

>}]

## Clothes Segmentation
For segmentation, please use the following format:
>[{
>>"image_id" : int,\
>>"category_id" : int,\
>>"segmentation" : RLE,\
>>"score" : float,

>}]

## Clothes Retrieval
For clothes retrieval, please use the following format:
>[{
>>"query_image_id" : int,\
>>"query_bbox" : [x1,y1,x2,y2],\
>>"query_score" : float,\
>>"gallery_image_id" : [int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int],\
>>"gallery_bbox":[ [x1,y1,x2,y2],...[] ]

>}]

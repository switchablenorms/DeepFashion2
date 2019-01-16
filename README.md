# DeepFashion2 Dataset
![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/deepfashion2_bigbang.png)

DeepFashion2 is a comprehensive fashion dataset. It contains 491K diverse images of 13 popular clothing categories from both 
commercial shopping stores and consumers. It totally has 801K clothing clothing items, where each item in an image is labeled 
with scale, occlusion, zoom-in, viewpoint, category, style, bounding box, dense landmarks and per-pixel mask.There are also 873K Commercial-Consumer clothes pairs.\
The dataset is split into a training set (391K images), a validation set (34k images), and a test set (67k images).\
Examples of DeepFashion2 are shown in Figure 1.

<p align='center'>Figure 1: Examples of DeepFashion2.</p>

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/annotation.jpg)
*<sub>From (1) to (4), each row represents clothes images with different variations. At each row, we partition the images into two groups, the left three columns represent clothes from commercial stores, while the right three columns are from customers.In each group, the three images indicate three levels of difficulty with respect to the corresponding variation.Furthermore, at each row, the items in these two groups of images are from the same clothing identity but from two different domains, that is, commercial and customer.The items of the same identity may have different styles such as color and printing.Each item is annotated with landmarks and masks.*
# Announcements
* xx-xx-xx Validation set of DeepFashion2 is released.
 
# Download the Data
Below provides the links to validation set. We will soon release training set and test set.
* Images(val_imags.zip)
* Annotations(val_annos.zip)

# Data Organization
Each image in seperate image set has a unique six-digit number such as 000001.jpg. A corresponding annotation file in json
format is provided in annotation set such as 000001.json. \
Each annotation file is organized as below: 
* **source**: a string, where 'shop' indicates that the image is from commercial store while 'user' indicates that the image is taken by users.
* **pair_id**: a number. Images from the same shop and their corresponding consumer-taken images have the same pair id.
  * item 1 
    * **category_name**: a string which indicates the category of the item.
    * **category_id**: a number which corresponds to the category name. In category_id, 1 represents short sleeve top, 2 represents long sleeve top, 3 represents short sleeve outwear, 4 represents long sleeve outwear, 5 represents vest, 6 represents sling, 7 represents shorts, 8 represents trousers, 9 represents skirt, 10 represents short sleeve dress, 11 represents long sleeve dress, 12 represents vest dress and 13 represents sling dress.
    * **style**: a number to distinguish between clothing items from images with the same pair id. Clothing items with different style numbers from images with the same pair id have different styles such as color, printing, and logo. In this way, a clothing item from shop images and a clothing item from user image are positive commercial-consumer pair if they have the same style number greater than 0 and they are from images with the same pair id.
    * **bounding_box**: [x1,y1,x2,y2]，where x1 and y_1 represent the lower left point coordinate of bounding box, x_2 and y_2 represent the upper right point coordinate of bounding box. 
    * **landmarks**: [x1,y1,v1,...,xn,yn,vn], where v represents the visibility: v=2 visible; v=1 occlusion; v=0 not labeled. We have different definitions of landmarks for different categories. The orders of landmark annotations are listed in figure 2.
    * **segmentation**: [[x1,y1,...xn,yn],[ ]], where [x1,y1,xn,yn] represents a polygon and a single clothing item may contain more than one polygon.
    * **scale**: a number, where 1 represents small scale, 2 represents modest scale and 3 represents large scale.
    * **occlusion**: a number, where 1 represents slight occlusion(including no occlusion), 2 represents medium occlusion and 3 represents heavy occlusion.
    * **zoom_in**: a number, where 1 represents no zoom-in, 2 represents medium zoom-in and 3 represents lagre zoom-in.
    * **viewpoint**: a number, where 1 represents no wear, 2 represents frontal viewpoint and 3 represents side or back viewpoint.
  * item 2\
  ...<br>
  * item n

The definition of landmarks and skeletons of 13 categories are shown below. The numbers in the figure represent the order of landmark annotations of each category in annotation file. A total of 294 landmarks covering 13 categories are defined.

<p align='center'>Figure 2: Definitions of landmarks and skeletons.</p>

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/cls.jpg)
In validation set, we provide query image names in [list_query.txt](https://github.com/switchablenorms/DeepFashion2/blob/master/data/val/list_query.txt) and gallery image names in [list_gallery.txt](https://github.com/switchablenorms/DeepFashion2/blob/master/data/val/list_gallery.txt). In Commercial-Consumer Clothes Retrieval benchmark, during evaluation, each query clothing item with style number greater than 0 has corresponding ground truth gallery clothing item, which has the same style and pair_id with the query clothing item. A query clothing item may have more than one ground truth gallery clothing item.

# Dataset Statistics
Tabel 1 shows the statistics of images and annotations in DeepFashion2.

<p align='center'>Table 1: Statistics of DeepFashion2.</p>

| | Train | Validation | Test | Overall |  
|---:|---:|---:|---:|---:|
|images|390,884|33,669|67,342|491,895|
|bboxes|636,624|54,910|109,198|800,732|
|landmarks|636,624|54,910|109,198|800,732|
|masks|636,624|54,910|109,198|800,732|
|pairs|685,584|62,563<br/>query: &nbsp;&nbsp;12,612<br/>gallery: 37,355|125,087<br/>query: &nbsp;&nbsp;24,416<br/>gallery: 43,608|873,234|

Figure 3 shows the statistics of different variations and the numbers of items of the 13 categories in DeepFashion2.

<p align='center'>Figure 3: Statistics of DeepFashion2.</p>

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/statistics_all.jpg)

# Benchmarks
## Clothes Detection
This task detects clothes in an image by predicting bounding boxes and category labels to each detected clothing item.
The evaluation metrics are the bounding box's average precision $ {AP}_{box}$,${AP}_{box}^{IoU=0.50}$,${AP}_{box}^{IoU=0.75} $.

<p align='center'>Table 2: Clothes detection on different validation subsets, including scale, occlusion, zoom-in, and viewpoint.</p>

|||<sub>Scale|||<sub>Occlusion|||<sub>Zoom_in|||<sub>Viewpoint||<sub>Overall|
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
||<sub>small|<sub>moderate|<sub>large|<sub>slight|<sub>medium|<sub>heavy|<sub>no|<sub>medium|<sub>large|<sub>no wear|<sub>frontal|<sub>side or back||
|${AP}_{box}$|<sub>0.527|<sub>0.719|<sub>0.738|<sub>0.712|<sub>0.654|<sub>0.372|<sub>0.713|<sub>0.581|<sub>0.402|<sub>0.438|<sub>0.716|<sub>0.671|<sub>0.667|
|${AP}_{box}^{IoU=0.50}$|<sub>0.678|<sub>0.874|<sub>0.865|<sub>0.844|<sub>0.810|<sub>0.531|<sub>0.870|<sub>0.697|<sub>0.498|<sub>0.499|<sub>0.875|<sub>0.837|<sub>0.814|
|${AP}_{box}^{IoU=0.75}$|<sub>0.627|<sub>0.831|<sub>0.833|<sub>0.812|<sub>0.768|<sub>0.433|<sub>0.826|<sub>0.663|<sub>0.458|<sub>0.484|<sub>0.831|<sub>0.779|<sub>0.773|

## Landmark and Pose Estimation
This task aims to predict landmarks for each detected clothing item in an each image.Similarly, we employ the evaluation metrics used by COCOfor human pose estimation by calculating the average precision for keypoints ${AP}_{pt}$,${AP}_{pt}^{OKS=0.50}$,${AP}_{pt}^{OKS=0.75}$ where OKS indicates the object landmark similarity.
## Clothes Segmentation
This task assigns a category label (including background label) to each pixel in an item.The evaluation metrics is the average precision including  ${AP}_{mask}$,${AP}_{mask}^{IoU=0.50}$,${AP}_{mask}^{IoU=0.75}$ computed over masks.
## Consumer-to-Shop Clothes Retrieval
Given a detected item from a consumer-taken photo, this task aims to search the commercial images in the gallery for the items that are corresponding to this detected item. In this task, top-k retrieval accuracy is employed as the evaluation metric. We emphasize the retrieval performance while still consider the influence of detector. If a clothing item fails to be detected, this query item is counted as missed.
# Citation
If you use the DeepFashion2 dataset in your work, please cite it as:
```
@article{DeepFashion2,
  author = {Yuying Ge and Ruimao Zhang and Xiaogang Wang and Xiaoou Tang and Ping Luo},
  title={DeepFashion2: A Versatile Benchmark for Detection, Pose Estimation, Segmentation and Retrieval of Clothing Images},
}
```
Please note that the article is in submission at present.

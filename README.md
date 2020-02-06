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
* **2020-2-6 We are holding DeepFashion2 challenges in CVPR 2020 Workshop including [Clothes Landmark Estimation](https://competitions.codalab.org/competitions/22966) and [Clothes Retrieval](https://competitions.codalab.org/competitions/22967). Detailed information is available in [Third Workshop on 
Computer Vision for Fashion, Art and Design](https://sites.google.com/view/cvcreative2020/home?authuser=0).**
* 2019-9-6 Baseline of released DeepFashion2 dataset is available.
* 2019-8-1 DeepFashion2 Challenge in 2019 ICCV Workshop ended.
* 2019-7-12 Due to the damage in CodaLab database, we have republished our competitions in DeepFashion2 Challenge. If you are participates of DeepFashion2 Challenge, please recreate an account and upload your results again in [Landmark Estimation](https://codalab.lri.fr/competitions/564) or [Clothes Retrieval](https://codalab.lri.fr/competitions/565).
* 2019-7-1 Test images of DeepFashion2 are released in [DeepFashion2 dataset](https://drive.google.com/drive/folders/125F48fsMBz2EF0Cpqk6aaHet5VH399Ok?usp=sharing). (Password for unzipping test files is the same as that for unzipping training and validation files.)
* 2019-5-28 Links to DeepFashion2 challenges in ICCV 2019 Workshop are released. Detailed information is available in [Second Workshop on 
Computer Vision for Fashion, Art and Design](https://sites.google.com/view/cvcreative/home?authuser=0).
* 2019-5-27 ICCV 2019 Workshop website is released: [Second Workshop on 
Computer Vision for Fashion, Art and Design](https://sites.google.com/view/cvcreative/home?authuser=0). Links to challenges will be released soon.
 
# Download the Data
DeepFashion2 dataset is available in [DeepFashion2 dataset](https://drive.google.com/drive/folders/125F48fsMBz2EF0Cpqk6aaHet5VH399Ok?usp=sharing). You need fill in the [form](https://docs.google.com/forms/d/e/1FAIpQLSeIoGaFfCQILrtIZPykkr8q_h9qQ5BoTYbjvf95aXbid0v2Bw/viewform?usp=sf_link) to get password for unzipping files. Please refer to Data Description below for detailed information about dataset.

# Data Organization
Each image in seperate image set has a unique six-digit number such as 000001.jpg. A corresponding annotation file in json
format is provided in annotation set such as 000001.json. \
Each annotation file is organized as below: 
* **source**: a string, where 'shop' indicates that the image is from commercial store while 'user' indicates that the image is taken by users.
* **pair_id**: a number. Images from the same shop and their corresponding consumer-taken images have the same pair id.
  * item 1 
    * **category_name**: a string which indicates the category of the item.
    * **category_id**: a number which corresponds to the category name. In category_id, 1 represents short sleeve top, 2 represents long sleeve top, 3 represents short sleeve outwear, 4 represents long sleeve outwear, 5 represents vest, 6 represents sling, 7 represents shorts, 8 represents trousers, 9 represents skirt, 10 represents short sleeve dress, 11 represents long sleeve dress, 12 represents vest dress and 13 represents sling dress.
    * **style**: a number to distinguish between clothing items from images with the same pair id. Clothing items with different style numbers from images with the same pair id have different styles such as color, printing, and logo. In this way, a clothing item from shop images and a clothing item from user image are positive commercial-consumer pair if they have the same style number greater than 0 and they are from images with the same pair id.(If you are confused with style, please refer to issue#10.) 
    * **bounding_box**: [x1,y1,x2,y2]，where x1 and y_1 represent the upper left point coordinate of bounding box, x_2 and y_2 represent the lower right point coordinate of bounding box. (width=x2-x1;height=y2-y1)
    * **landmarks**: [x1,y1,v1,...,xn,yn,vn], where v represents the visibility: v=2 visible; v=1 occlusion; v=0 not labeled. We have different definitions of landmarks for different categories. The orders of landmark annotations are listed in figure 2.
    * **segmentation**: [[x1,y1,...xn,yn],[ ]], where [x1,y1,xn,yn] represents a polygon and a single clothing item may contain more than one polygon.
    * **scale**: a number, where 1 represents small scale, 2 represents modest scale and 3 represents large scale.
    * **occlusion**: a number, where 1 represents slight occlusion(including no occlusion), 2 represents medium occlusion and 3 represents heavy occlusion.
    * **zoom_in**: a number, where 1 represents no zoom-in, 2 represents medium zoom-in and 3 represents lagre zoom-in.
    * **viewpoint**: a number, where 1 represents no wear, 2 represents frontal viewpoint and 3 represents side or back viewpoint.
  * item 2\
  ...<br>
  * item n

Please note that 'pair_id' and 'source' are image-level labels. All clothing items in an image share the same 'pair_id' and 'source'.  

The definition of landmarks and skeletons of 13 categories are shown below. The numbers in the figure represent the order of landmark annotations of each category in annotation file. A total of 294 landmarks covering 13 categories are defined.

<p align='center'>Figure 2: Definitions of landmarks and skeletons.</p>

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/cls.jpg)

We do not provide data in pairs. In training dataset, images are organized with continuous 'pair_id' including images from consumers and images from shops. (For example: 000001.jpg(pair_id:1; from consumer), 000002.jpg(pair_id:1; from shop),000003.jpg(pair_id:2; from consumer),000004.jpg(pair_id:2; from consumer),000005.jpg(pair_id:2; from consumer), 000006.jpg(pair_id:2; from consumer),000007.jpg(pair_id:2; from shop),000008.jpg(pair_id:2; from shop)...) A clothing item from shop images and a clothing item from consumer image are positive commercial-consumer pair if they have the same style number which is greater than 0 and they are from images with the same pair id, otherwise they are negative pairs. In this way, you can construct training positive pairs and negative pairs in instance-level.

As is shown in the figure below, the first three images are from consumers and the last two images are from shops. These five images have the same 'pair_id'. Clothing items in orange bounding box have the same 'style':1. Clothing items in green bounding box have the same 'style': 2. 'Style' of other clothing items whose bouding boxes are not drawn in the figure is 0 and they can not construct positive commercial-consumer pairs. One positive commercial-consumer pair is the annotated short sleeve top in the first image and the annotated short sleeve top in the last image. Our dataset makes it possbile to construct instance-level pairs in a flexible way.

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/pair.jpg)

# Data Description
Training images: train/image              Training annotations: train/annos

Validation images: validation/image   Validation annotations: validation/annos

Test images: test/image

Each image in seperate image set has a unique six-digit number such as 000001.jpg. A corresponding annotation file in json format is provided in annotation set such as 000001.json. We provide code to generate coco-type annotations from our dataset in [deepfashion2_to_coco.py](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/deepfashion2_to_coco.py). Please note that during evaluation, image_id is the digit number of the image name. (For example, the image_id of image 000001.jpg is 1). Json files in json_for_validation and json_for_test are generated based on the above rule using [deepfashion2_to_coco.py](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/deepfashion2_to_coco.py). In this way, you can generate groundtruth json files for evaluation for clothes detection task and clothes segmentation task, which are not listed in DeepFashion2 Challenge.

In validation set, we provide image-level information in keypoints_val_information.json, retrieval_val_consumer_information.json and retrieval_val_shop_information.json. ( In validation set, the first 10844 images are from consumers and the last 20681 images are from shops.) For clothes detection task and clothes segmentation task, which are not listed in DeepFashion2 Challenge, keypoints_val_information.json can also be used.

We provide keypoints_val_vis.json, keypoints_val_vis_and_occ.json, val_query.json and val_gallery.json for evaluation of validation set. You can get validation score locally using  [Evaluation Code](https://github.com/switchablenorms/DeepFashion2/blob/master/evaluation/evaluation.md) and above json files. You can also submit your results to evaluation server in our DeepFashion2 Challenge.

In test set, we provide image-level information in keypoints_test_information.json, retrieval_test_consumer_information.json and retrieval_test_shop_information.json.( In test set, the first 20681 images are from consumers and the last 41948 images are from shops.) You need submit your results to evaluation server in our DeepFashion2 Challenge.

# Dataset Statistics
Tabel 1 shows the statistics of images and annotations in DeepFashion2. (For statistics of released images and annotations, please refer to [DeepFashion2 Challenge](https://sites.google.com/view/cvcreative/deepfashion2?authuser=0)).

<p align='center'>Table 1: Statistics of DeepFashion2.</p>

| | Train | Validation | Test | Overall |  
|---:|---:|---:|---:|---:|
|images|390,884|33,669|67,342|491,895|
|bboxes|636,624|54,910|109,198|800,732|
|landmarks|636,624|54,910|109,198|800,732|
|masks|636,624|54,910|109,198|800,732|
|pairs|685,584|query: 12,550<br/>gallery: 37183|query: 24,402<br/>gallery: 75,347|873,234|

Figure 3 shows the statistics of different variations and the numbers of items of the 13 categories in DeepFashion2.

<p align='center'>Figure 3: Statistics of DeepFashion2.</p>

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/statistics_all.jpg)

# Benchmarks
## Clothes Detection
This task detects clothes in an image by predicting bounding boxes and category labels to each detected clothing item.
The evaluation metrics are the bounding box's average precision <a href="https://www.codecogs.com/eqnedit.php?latex=$&space;{AP}_{box}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$&space;{AP}_{box}$" title="$ {AP}_{box}$" /></a>,<a href="https://www.codecogs.com/eqnedit.php?latex=${AP}_{box}^{IoU=0.50}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?${AP}_{box}^{IoU=0.50}$" title="${AP}_{box}^{IoU=0.50}$" /></a>,<a href="https://www.codecogs.com/eqnedit.php?latex=${AP}_{box}^{IoU=0.75}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?${AP}_{box}^{IoU=0.75}$" title="${AP}_{box}^{IoU=0.75}$" /></a>.

<p align='center'>Table 2: Clothes detection trained with released DeepFashion2 Dataset evaluated on validation set.</p>

| AP | AP50 | AP75 | 
|---:|---:|---:|
|0.638|0.789|0.745|

<p align='center'>Table 3: Clothes detection on different validation subsets, including scale, occlusion, zoom-in, and viewpoint.</p>

|||<sub>Scale|||<sub>Occlusion|||<sub>Zoom_in|||<sub>Viewpoint||<sub>Overall|
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
||<sub>small|<sub>moderate|<sub>large|<sub>slight|<sub>medium|<sub>heavy|<sub>no|<sub>medium|<sub>large|<sub>no wear|<sub>frontal|<sub>side or back||
|<sub>AP|<sub>0.604|<sub>0.700|<sub>0.660|<sub>0.712|<sub>0.654|<sub>0.372|<sub>0.695|<sub>0.629|<sub>0.466|<sub>0.624|<sub>0.681|<sub>0.641|<sub>0.667|
|<sub>AP50|<sub>0.780|<sub>0.851|<sub>0.768|<sub>0.844|<sub>0.810|<sub>0.531|<sub>0.848|<sub>0.755|<sub>0.563|<sub>0.713|<sub>0.832|<sub>0.796|<sub>0.814|
|<sub>AP75|<sub>0.717|<sub>0.809|<sub>0.744|<sub>0.812|<sub>0.768|<sub>0.433|<sub>0.806|<sub>0.718|<sub>0.525|<sub>0.688|<sub>0.791|<sub>0.744|<sub>0.773

## Landmark and Pose Estimation
This task aims to predict landmarks for each detected clothing item in an each image.Similarly, we employ the evaluation metrics used by COCOfor human pose estimation by calculating the average precision for keypoints <a href="https://www.codecogs.com/eqnedit.php?latex=${AP}_{pt}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?${AP}_{pt}$" title="${AP}_{pt}$" /></a>,<a href="https://www.codecogs.com/eqnedit.php?latex=${AP}_{pt}^{OKS=0.50}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?${AP}_{pt}^{OKS=0.50}$" title="${AP}_{pt}^{OKS=0.50}$" /></a>,<a href="https://www.codecogs.com/eqnedit.php?latex=${AP}_{pt}^{OKS=0.75}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?${AP}_{pt}^{OKS=0.75}$" title="${AP}_{pt}^{OKS=0.75}$" /></a> where OKS indicates the object landmark similarity.

<p align='center'>Table 4: Landmark estimation trained with released DeepFashion2 Dataset evaluated on validation set.</p>

| | AP | AP50 | AP75 | 
|---:|---:|---:|---:|
|vis|0.605|0.790|0.684|
|vis && hide|0.529|0.775|0.596|

<p align='center'>Table 5: Landmark Estimation on different validation subsets, including scale, occlusion, zoom-in, and viewpoint.Results of evaluation on visible landmarks only and evaluation on both visible and occlusion landmarks are separately shown in each row</p>

|||<sub>Scale|||<sub>Occlusion|||<sub>Zoom_in|||<sub>Viewpoint||<sub>Overall|
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
||<sub>small|<sub>moderate|<sub>large|<sub>slight|<sub>medium|<sub>heavy|<sub>no|<sub>medium|<sub>large|<sub>no wear|<sub>frontal|<sub>side or back||
 |<sub>AP|<sub>0.587<br/>0.497|<sub>0.687<br/>0.607|<sub>0.599<br/>0.555|<sub>0.669<br/>0.643|<sub>0.631<br/>0.530|<sub>0.398<br/>0.248|<sub>0.688<br/>0.616|<sub>0.559<br/>0.489|<sub>0.375<br/>0.319|<sub>0.527<br/>0.510|<sub>0.677<br/>0.596|<sub>0.536<br/>0.456|<sub>0.641<br/>0.563|
|<sub>AP50|<sub>0.780<br/>0.764|<sub>0.854<br/>0.839|<sub>0.782<br/>0.774|<sub>0.851<br/>0.847|<sub>0.813<br/>0.799|<sub>0.534<br/>0.479|<sub>0.855<br/>0.848|<sub>0.757<br/>0.744|<sub>0.571<br/>0.549|<sub>0.724<br/>0.716|<sub>0.846<br/>0.832|<sub>0.748<br/>0.727|<sub>0.820<br/>0.805|
|<sub>AP75|<sub>0.671<br/>0.551|<sub>0.779<br/>0.703|<sub>0.678<br/>0.625|<sub>0.760<br/>0.739|<sub>0.718<br/>0.600|<sub>0.440<br/>0.236|<sub>0.786<br/>0.714|<sub>0.633<br/>0.537|<sub>0.390<br/>0.307|<sub>0.571<br/>0.550|<sub>0.771<br/>0.684|<sub>0.610<br/>0.506|<sub>0.728<br/>0.641|
 
Figure 4 shows the results of landmark and pose estimation.

<p align='center'>Figure 4: Results of landmark and pose estimation.</p>

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/keys_vis.jpg)

## Clothes Segmentation
This task assigns a category label (including background label) to each pixel in an item.The evaluation metrics is the average precision including <a href="https://www.codecogs.com/eqnedit.php?latex=${AP}_{mask}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?${AP}_{mask}$" title="${AP}_{mask}$" /></a>,<a href="https://www.codecogs.com/eqnedit.php?latex=${AP}_{mask}^{IoU=0.50}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?${AP}_{mask}^{IoU=0.50}$" title="${AP}_{mask}^{IoU=0.50}$" /></a>,<a href="https://www.codecogs.com/eqnedit.php?latex=${AP}_{mask}^{IoU=0.75}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?${AP}_{mask}^{IoU=0.75}$" title="${AP}_{mask}^{IoU=0.75}$" /></a> computed over masks.

<p align='center'>Table 6: Clothes segmentation trained with released DeepFashion2 Dataset evaluated on validation set.</p>

| AP | AP50 | AP75 | 
|---:|---:|---:|
|0.640|0.797|0.754|

<p align='center'>Table 7: Clothes Segmentation on different validation subsets, including scale, occlusion, zoom-in, and viewpoint.</p>

|||<sub>Scale|||<sub>Occlusion|||<sub>Zoom_in|||<sub>Viewpoint||<sub>Overall|
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
||<sub>small|<sub>moderate|<sub>large|<sub>slight|<sub>medium|<sub>heavy|<sub>no|<sub>medium|<sub>large|<sub>no wear|<sub>frontal|<sub>side or back||
|<sub>AP|<sub>0.634|<sub>0.703|<sub>0.666|<sub>0.720|<sub>0.656|<sub>0.381|<sub>0.701|<sub>0.637|<sub>0.478|<sub>0.664|<sub>0.689|<sub>0.635|<sub>0.674|
|<sub>AP50|<sub>0.811|<sub>0.865|<sub>0.798|<sub>0.863|<sub>0.824|<sub>0.543|<sub>0.861|<sub>0.791|<sub>0.591|<sub>0.757|<sub>0.849|<sub>0.811|<sub>0.834|
|<sub>AP75|<sub>0.752|<sub>0.826|<sub>0.773|<sub>0.836|<sub>0.780|<sub>0.444|<sub>0.823|<sub>0.751|<sub>0.559|<sub>0.737|<sub>0.810|<sub>0.755|<sub>0.793|
 
Figure 5 shows the results of clothes segmentation.

<p align='center'>Figure 5: Results of clothes segmentation.</p>

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/seg_vis.jpg)
 
## Consumer-to-Shop Clothes Retrieval
Given a detected item from a consumer-taken photo, this task aims to search the commercial images in the gallery for the items that are corresponding to this detected item. In this task, top-k retrieval accuracy is employed as the evaluation metric. We emphasize the retrieval performance while still consider the influence of detector. If a clothing item fails to be detected, this query item is counted as missed.

<p align='center'>Table 8: Consumer-to-Shop Clothes Retrieval trained with released DeepFashion2 Dataset using detected box evaluated on validation set.</p>

| | Top-1 | Top-5 | Top-10 | Top-15 | Top-20 | 
|---:|---:|---:|---:|---:|---:|
|class|0.079|0.198|0.273|0.329|0.366|
|keypoints|0.182|0.326|0.416|0.469|0.510|
|segmentation|0.135|0.271|0.350|0.407|0.447|
|class+keys|0.192|0.345|0.435|0.488|0.524|
|class+seg|0.152|0.295|0.379|0.435|0.477|

<p align='center'>Table 9: Consumer-to-Shop Clothes Retrieval on different subsets of some validation consumer-taken images. Each query item in these images has over 5 identical clothing items in validation commercial images. Results of evaluation on ground truth box and detected box are separately shown in each row. The evaluation metrics are top-20 accuracy.</p>

|||<sub>Scale|||<sub>Occlusion|||<sub>Zoom_in|||<sub>Viewpoint|||<sub>Overall||
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
||<sub>small|<sub>moderate|<sub>large|<sub>slight|<sub>medium|<sub>heavy|<sub>no|<sub>medium|<sub>large|<sub>no wear|<sub>frontal|<sub>side or back|<sub>top-1|<sub>top-10|<sub>top-20||
|<sub>class|<sub>0.520<br/>0.485|<sub>0.630<br/>0.537|<sub>0.540<br/>0.502|<sub>0.572<br/>0.527|<sub>0.563<br/>0.508|<sub>0.558<br/>0.383|<sub>0.618<br/>0.553|<sub>0.547<br/>0.496|<sub>0.444<br/>0.405|<sub>0.546<br/>0.499|<sub>0.584<br/>0.523|<sub>0.533<br/>0.487|<sub>0.102<br/>0.091|<sub>0.361<br/>0.312|<sub>0.470<br/>0.415|
|<sub>pose|<sub>0.721<br/>0.637|<sub>0.778<br/>0.702|<sub>0.735<br/>0.691|<sub>0.756<br/>0.710|<sub>0.737<br/>0.670|<sub>0.728<br/>0.580|<sub>0.775<br/>0.710|<sub>0.751<br/>0.701|<sub>0.621<br/>0.560|<sub>0.731<br/>0.690|<sub>0.763<br/>0.700|<sub>0.711<br/>0.645|<sub>0.264<br/>0.243|<sub>0.562<br/>0.497|<sub>0.654<br/>0.588|
|<sub>mask|<sub>0.624<br/>0.552|<sub>0.714<br/>0.657|<sub>0.646<br/>0.608|<sub>0.675<br/>0.639|<sub>0.651<br/>0.593|<sub>0.632<br/>0.555|<sub>0.711<br/>0.654|<sub>0.655<br/>0.613|<sub>0.526<br/>0.495|<sub>0.644<br/>0.615|<sub>0.682<br/>0.630|<sub>0.637<br/>0.565|<sub>0.193<br/>0.186|<sub>0.474<br/>0.422|<sub>0.571<br/>0.520|
|<sub>pose+class|<sub>0.752<br/>0.691|<sub>0.786<br/>0.730|<sub>0.733<br/>0.705|<sub>0.754<br/>0.725|<sub>0.750<br/>0.706|<sub>0.728<br/>0.605|<sub>0.789<br/>0.746|<sub>0.750<br/>0.709|<sub>0.620<br/>0.582|<sub>0.726<br/>0.699|<sub>0.771<br/>0.723|<sub>0.719<br/>0.684|<sub>0.268<br/>0.244|<sub>0.574<br/>0.522|<sub>0.665<br/>0.617|
|<sub>mask+class|<sub>0.656<br/>0.610|<sub>0.728<br/>0.666|<sub>0.687<br/>0.649|<sub>0.714<br/>0.676|<sub>0.676<br/>0.623|<sub>0.654<br/>0.549|<sub>0.725<br/>0.674|<sub>0.702<br/>0.655|<sub>0.565<br/>0.536|<sub>0.684<br/>0.648|<sub>0.712<br/>0.661|<sub>0.658<br/>0.604|<sub>0.212<br/>0.208|<sub>0.496<br/>0.451|<sub>0.595<br/>0.542|

Figure 6 shows queries with top-5 retrieved clothing items. The first and the seventh column are the images from the customers with bounding boxes predicted by detection module, and the second to the sixth columns and the eighth to the twelfth columns show the retrieval results from the store.

<p align='center'>Figure 6: Results of clothes retrieval.</p>

![image](https://github.com/switchablenorms/DeepFashion2/blob/master/images/retrieval_vis.jpg)

# Citation
If you use the DeepFashion2 dataset in your work, please cite it as:
```
@article{DeepFashion2,
  author = {Yuying Ge and Ruimao Zhang and Lingyun Wu and Xiaogang Wang and Xiaoou Tang and Ping Luo},
  title={A Versatile Benchmark for Detection, Pose Estimation, Segmentation and Re-Identification of Clothing Images},
  journal={CVPR},
  year={2019}
}
```

<h2>TensorFlow-FlexUNet-Image-Segmentation-UWM-GI-Tract (2026/08/14)</h2>
Sarah T. Arai<br>
Software Laboratory antillia.com<br><br>
This is the first experiment of Image Segmentation for <b>UW-Madison GI Tract Image</b>  
based on our <a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Model">
TensorFlow-FlexUNet-Image-Segmentation-Model</a> (TensorFlow Flexible UNet Image Segmentation Model for Multiclass) , 
and a 512x512 pixels upscaled <a href="https://drive.google.com/file/d/1yiy_7KxHn1X4wLFNzJNdRlHCJik69kbA/view?usp=sharing">
<b>UWM-GI-Tract-ImageMask-Dataset.zip</b></a> with colorized masks, which was derived by us from <br><br>
<a href="https://www.kaggle.com/datasets/purplejester/uwm-images-and-masks">
<b>UWM Images and Masks</b>
</a> by Ilia Zaitsev.
<br><br>
<hr>
<b>Actual Image Segmentation for UWM-GI-Tract Images of 512x512 pixels</b><br>
As shown below, the inferred masks predicted by our segmentation model trained by our dataset appear 
similar to the ground truth masks.<br><br>
<b>class_color_map = {Small_Bowel:yellow, Large_Bowel:green, Stomach:red}</b><br>
<br>
<table>
<tr>
<th>Input: image</th>
<th>Mask (ground_truth)</th>
<th>Prediction: inferred_mask</th>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case11_day12_slice_0101.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case11_day12_slice_0101.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case11_day12_slice_0101.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case117_day16_slice_0038.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case117_day16_slice_0038.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case117_day16_slice_0038.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case121_day14_slice_0086.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case121_day14_slice_0086.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case121_day14_slice_0086.png" width="320" height="auto"></td>
</tr>
</table>
<hr>
<br>
<h3>1  Dataset Citation</h3>
The dataset used here was derived from <br><br>
<a href="https://www.kaggle.com/datasets/purplejester/uwm-images-and-masks">
<b>UWM Images and Masks</b>
</a> <br>
UW-Madison GI Tract Image Segmentation: Preprocessed Dataset
<br>by Ilia Zaitsev.
<br><br>
The following explanation was taken from the website above.<br><br>

<b>About Dataset</b><br>
This dataset is a pre-processed version of the 
<a href="https://www.kaggle.com/competitions/uw-madison-gi-tract-image-segmentation">
UW-Madison GI Tract Image Segmentation data.</a>
<br>
It has the following structure:<br>
<ul>
<li>image_props.csv - some basic information about sample</li>
<li>images - samples in PNG format (same as the original dataset)</li>
<li>masks - decoded masks in PNG format (the original dataset provides them in RLE format)</li>
</ul>
This derived dataset is created to make it a bit simpler to work with than the original. All rights reserved to the respective owners.
<br><br>
<b>Acknowledgments:</b><br>
Sangjune Laurence Lee MSE MD FRCPC DABR<br>
Poonam Yadav Ph.D., DABR<br>
Yin Li PhD<br>
Jason J. Meudt BS, RTT<br>
Jessica Strang<br>
Dustin Hebel<br>
Alyx Alfson MS CMD, R.T.(T)<br>
Stephanie J. Olson RTT (BS), CMD (MS)<br>
Tera R. Kruser MS, RTT, CMD<br>
Jennifer B Smilowitz, Ph.D., DABR, FAAPM<br>
Kailee Borchert<br>
Brianne Loritz<br>
John Bayouth PhD<br>
Michael Bassetti MD PhD<br><br>
Work funded by the University of Wisconsin Carbone Cancer Center Pancreas Pilot Research Grant.

<br><br>
<b>License</b><br>
Data files © Original Authors<br>
<br>
<h3>
2 UWM-GI-Tract ImageMask Dataset
</h3>
 If you would like to train this UWM-GI-Tract Segmentation model by yourself,
 please download the original dataset from the google drive  
<a href="https://drive.google.com/file/d/1yiy_7KxHn1X4wLFNzJNdRlHCJik69kbA/view?usp=sharing">
<b>UWM-GI-Tract-ImageMask-Dataset.zip</b></a>
, expand the downloaded, and put it under <b>./dataset </b> folder to be:<br>
<pre>
./dataset
└─UWM-GI-Tract
    ├─test
    │   ├─images
    │   └─masks
    ├─train
    │   ├─images
    │   └─masks
    └─valid
        ├─images
        └─masks
</pre>
<br>
<b>UWM-GI-Tract Statistics</b><br>
<img src ="./projects/TensorFlowFlexUNet/UWM-GI-Tract/UWM-GI-Tract_Statistics.png" width="512" height="auto"><br>
<br>
As shown above, the number of images of train and valid datasets is large enough to use for a training set of our segmentation model.
<br>
<br>
<b>Train_images_sample</b><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/train_images_sample.png" width="1024" height="auto">
<br>
<b>Train_masks_sample</b><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/train_masks_sample.png" width="1024" height="auto">
<br>
<h3>
3 Train TensorflowFlexUNet Model
</h3>
 We trained UWM-GI-Tract TensorflowFlexUNet Model by using the following
<a href="./projects/TensorFlowFlexUNet/UWM-GI-Tract/train_eval_infer.config"> <b>train_eval_infer.config</b></a> file. <br>
Please move to <b>./projects/TensorFlowFlexUNet/UWM-GI-Tract</b> folder and run the following bat file.<br>
<pre>
>1.train.bat
</pre>
, which simply runs the following command.<br>
<pre>
>python ../../../src/TensorFlowFlexUNetTrainer.py ./train_eval_infer.config
</pre>
<hr>
<b>Model parameters</b><br>
Defined a small <b>base_filters=16</b> and a large <b>base_kernels=(11,11)</b> for the first Conv Layer of Encoder Block of 
<a href="./src/TensorFlowFlexUNet.py">TensorFlowFlexUNet.py</a> 
and a large <b>num_layers=8</b> (including a bridge between Encoder and Decoder Blocks).
<pre>
[model]
image_width    = 512
image_height   = 512
image_channels = 3
input_normalize = True
normalization  = False
num_classes    = 4
base_filters   = 16
base_kernels   = (11,11)
num_layers     = 8
dropout_rate   = 0.05
dilation       = (1,1)
</pre>

<b>Learning rate</b><br>
Defined a small learning rate.  
<pre>
[model]
learning_rate  = 0.00007
</pre>

<b>Loss and metrics functions</b><br>
Specified "categorical_crossentropy" and "dice_coef_multiclass".<br>
<pre>
[model]
loss           = "categorical_crossentropy"
metrics        = ["dice_coef_multiclass"]
</pre>
<b >Learning rate reducer callback</b><br>
Enabled learing_rate_reducer callback, and a small reducer_patience.
<pre> 
[train]
learning_rate_reducer = True
reducer_factor     = 0.5
reducer_patience   = 4
</pre>
<b>Early stopping callback</b><br>
Enabled early stopping callback with patience parameter.
<pre>
[train]
patience      = 10
</pre>
<b></b><br>
<b>RGB color map</b><br>
rgb color map dict for UWM-GI-Tract 1+3 classes.<br>
<pre>
[mask]
mask_file_format = ".png"
;UWM-GI-Tract 1+3               
; Background:black, Small_Bowel:yellow, Large_Bowel:green, Stomach:red
rgb_map = {(0,0,0):0,(255,255,0):1,(0,200,0):2255,0,0):3}
</pre>
<b>Epoch change inference callbacks</b><br>
Enabled epoch_change_infer callback.<br>
<pre>
[train]
epoch_change_infer       = True
epoch_change_infer_dir   =  "./epoch_change_infer"
epoch_changeinfer        = False
epoch_changeinfer_dir    = "./epoch_changeinfer"
num_infer_images         = 6
</pre>
By using this epoch_change_infer callback, on every epoch_change, the inference procedure can be called
 for 6 images in <b>mini_test</b> folder. This will help you confirm how the predicted mask changes 
 at each epoch during your training process.<br> <br> 
<b>Epoch_change_inference output at starting (1,2,3)</b><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/epoch_change_infer_at_start.png" width="1024" height="auto"><br>
<br>
<b>Epoch_change_inference output at ending (18,19,20)</b><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/epoch_change_infer_at_middlepoint.png" width="1024" height="auto"><br>
<br>
<b>Epoch_change_inference output at ending (38,39,40)</b><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/epoch_change_infer_at_end.png" width="1024" height="auto"><br>

<br>
In this experiment, the training process was terminated at epoch 40.<br><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/train_console_output_at_epoch40.png" width="880" height="auto"><br>
<br>
<a href="./projects/TensorFlowFlexUNet/UWM-GI-Tract/eval/train_metrics.csv">train_metrics.csv</a><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/eval/train_metrics.png" width="520" height="auto"><br>

<br>
<a href="./projects/TensorFlowFlexUNet/UWM-GI-Tract/eval/train_losses.csv">train_losses.csv</a><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/eval/train_losses.png" width="520" height="auto"><br>
<br>
<h3>
4 Evaluation
</h3>
Please move to <b>./projects/TensorFlowFlexUNet/UWM-GI-Tract</b> folder,
and run the following bat file to evaluate TensorflowFlexUNet model for UWM-GI-Tract.<br>
<pre>
>./2.evaluate.bat
</pre>
This bat file simply runs the following command.
<pre>
>python ../../../src/TensorFlowFlexUNetEvaluator.py  ./train_eval_infer.config
</pre>
Evaluation console output:<br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/evaluate_console_output_at_epoch40.png" width="880" height="auto">
<br><br>Image-Segmentation-UWM-GI-Tract
<a href="./projects/TensorFlowFlexUNet/UWM-GI-Tract/evaluation.csv">evaluation.csv</a><br>
The loss (categorical_crossentropy) to this UWM-GI-Tract/test was low, and dice_coef_multiclass high as shown below.
<br>
<pre>
categorical_crossentropy,0.0215
dice_coef_multiclass,0.9894
</pre>
<br>
<h3>5 Inference</h3>
Please move to <b>./projects/TensorFlowFlexUNet/UWM-GI-Tract</b> folder 
,and run the following bat file to infer segmentation regions for images by the Trained-TensorflowFlexUNet model for UWM-GI-Tract.<br>
<pre>
>./3.infer.bat
</pre>
This simply runs the following command.
<pre>
>python ../../../src/TensorFlowFlexUNetInferencer.py ./train_eval_infer.config
</pre>
<hr>
<b>mini_test_images</b><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/mini_test_images.png" width="1024" height="auto"><br>
<b>mini_test_mask(ground_truth)</b><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/mini_test_masks.png" width="1024" height="auto"><br>
<hr>
<b>Inferred test masks</b><br>
<img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/asset/mini_test_output.png" width="1024" height="auto"><br>
<br>
<hr>
<b>Enlarged images and masks for UWM-GI-Tract Images of 650x650 pixels</b><br>
As shown below, the inferred masks predicted by our segmentation model trained by our dataset appear similar to the ground truth masks.
<br>
<br>
<b>class_color_map = {Small_Bowel:yellow, Large_Bowel:green, Stomach:red}</b><br><br>
<table>
<tr>
<th>Input: image</th>
<th>Mask (ground_truth)</th>
<th>Prediction: inferred_mask</th>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case101_day20_slice_0078.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case101_day20_slice_0078.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case101_day20_slice_0078.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case107_day19_slice_0093.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case107_day19_slice_0093.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case107_day19_slice_0093.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case117_day0_slice_0074.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case117_day0_slice_0074.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case117_day0_slice_0074.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case117_day16_slice_0038.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case117_day16_slice_0038.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case117_day16_slice_0038.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case118_day14_slice_0097.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case118_day14_slice_0097.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case118_day14_slice_0097.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/images/case121_day14_slice_0086.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test/masks/case121_day14_slice_0086.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UWM-GI-Tract/mini_test_output/case121_day14_slice_0086.png" width="320" height="auto"></td>
</tr>
</table>
<hr>
<br>
<h3>
References
</h3>
<b>1. UW-Madison_GI_Tract_Image_Segmentation</b><br>
OpenMEDLab<br>
<a href="https://github.com/openmedlab/Awesome-Medical-Dataset/blob/main/resources/UW-Madison_GI_Tract_Image_Segmentation.md">
https://github.com/openmedlab/Awesome-Medical-Dataset/blob/main/resources/UW-Madison_GI_Tract_Image_Segmentation.md</a>
<br>
<br>
<b>2. TensorFlow-FlexUNet-Image-Segmentation-CURVAS-MICCAI2024-Abdominal-MultiOrgan </b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-CURVAS-MICCAI2024-Abdominal-MultiOrgan">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-CURVAS-MICCAI2024-Abdominal-MultiOrgan</a>
<br>
<br>
<b>3. TensorFlow-FlexUNet-Image-Segmentation-Synapse-Abdominal-MultiOrgan</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Synapse-Abdominal-MultiOrgan">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Synapse-Abdominal-MultiOrgan</a>
<br>
<br>
<b>4. TensorFlow-FlexUNet-Image-Segmentation-Model</b><br>
Toshiyuki Arai <br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Model">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Model
</a>
<br>
<br>

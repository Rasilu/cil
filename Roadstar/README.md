# Running the source code
The models folder of our submitted code contains two ipynb notebooks, CIL\_UNets and CIL\_segformer, one for the various U-Net architectures and one for the segformer. The datasets used are fetched from a github repo when running the notebooks.

To reproduce our tests in the U-Net notebook, simply set the MODEL and LOSS\_FN parameters accordingly. All Other parameters that can be changed in the configuration (such as BATCH\_SIZE, POSTPROCESSING\_MAJORITY, PREPROCESS\_GAUSSIAN\_BLUR\_KERNEL\_SIZE) were set as provided in the notebook for all our tests. However, we include the ability to configure these parameters for future use.

To reproduce our experiments for the SegFormer model, simply run the included notebook directly. As the SegFormer model is based on an existing pretrained model and is intended to be used mainly to support the failure modes of Unet-3+RS, there are no hyperparameters to be set in this notebook and it has already been tuned.

The "code" folder in our submission includes the supplementary notebook used to generate the image similarity scores for preprocessing, the script to predict using an ensemble model and some other utilities, such as chunking commits to Github in order to make the datasets remotely available to our notebooks.


# Creating a Ensemble Prediction
The best-performing model on Kaggle is a majority voting based ensemble model. It's implemented by taking the predictions of multiple models and then doing a majority voting on the hard labels. To generate an ensemble prediction, add the predictions of the individual models to the "predictions" folder and run the script. To give an individual model more weight, that models prediction can be copied into the folder multiple times.

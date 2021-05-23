# ⌚ Detecting compulsive behaviors with smartwatches
![header image](https://github.com/Bhorda/BFRBAnticipationDataset/blob/main/BFRB_Detection_Data/figure.png)

### 📖 Anticipatory Detection of Compulsive Body-focused Repetitive Behaviors with Wearables

<details><summary>Abstract (click to expand)</summary>
<p>

Body-focused repetitive behaviors (BFRBs), like face-touching or skin-picking, are hand-driven behaviors which can damage one’s
appearance, if not identified early and treated. Technology for automatic detection is still under-explored, with few previous works
being limited to wearables with single modalities (e.g., motion). Here, we propose a multi-sensory approach combining motion,
orientation, and heart rate sensors to detect BFRBs. We conducted a feasibility study in which participants (N=10) were exposed to
BFRBs-inducing tasks, and analyzed 380 mins of signals under an extensive evaluation of sensing modalities, cross-validation methods,
and observation windows. Our models achieved an AUC > 0.90 in distinguishing BFRBs, which were more evident in observation
windows 5 mins prior to the behavior as opposed to 1-min ones. In a follow-up qualitative survey, we found that not only the timing
of detection matters but also models need to be context-aware, when designing just-in-time interventions to prevent BFRBs.

</p>
</details>

**This repository**. We provide the dataset and some pre-processing code to reproduce the experiments of our paper [1]. The main input is data collected from a Samsung Galaxy watch which recorded acceleration, gyroscope, and heart rate signals. After our participants completed a set of tasks designed to incuce BRFBs, we annotated the sensor data with BFRB labels through a video recording. Here, we provide the timestamps along with the labeled timeseries for each sensor modality. To facilitate easier re-use of this dataset, we also provide the data pipeline code which creates positive and negative windows, extracts features, and further normalizes the resulting feature vectors in order to prepare them for machine learning.

## 🛠️ Requirements
The code is written in python X.X.X. The main libraries needed to execute our code are as follows:

 - numpy XXX
 - pandas XXX
 - ...

## 🗂️ Data 
The sensor signals can be found in ``BFRB_Detection_Data``. Each participant's data in ``data/exp-X`` contains 5 .csv files which include the accelerometer, gyroscope, heart rate, and heart rate variability signals, along with the raw timestamps.

# ▶️ Run 

To produce the final feature vectors used in our study plese navigate to ``BFRB_Detection_Data/pipeline`` and run:

    python 1+_WindowSplit.py
    python 1-_WindowSplit.py
    python 2_FeatureExtraction.py
    python 3_Normalization.py
    
   
## How to cite our paper 

Please cite our paper if you use data/code from this project:

> [1]  Benjamin Searle, Dimitris Spathis, Marios Constantinides, Daniele Quercia, Cecilia Mascolo. 2021. ["Anticipatory Detection of Compulsive Body-focused Repetitive Behaviors with Wearables."](https://mobilehci.acm.org/2021) In Proceedings of ACM International Conference on Mobile Human-Computer Interaction (MobileHCI 2021). (to appear)

## License

This data and code release is licensed under the terms and conditions of MIT unless otherwise stated. The actual paper is governed by a separate license and the paper authors retain their respective copyrights.   
    

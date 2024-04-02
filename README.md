## Radiomic Cardiac MR Imaging Signatures of Ventricular Arrhythmia in Non-Ischemic Cardiomyopathy


## Description of Code

This python/R code implements our logistic regression models for the prediction of ventricular arrhythmia.
First, radiomic features should be extracted using compute_radiomic_features.py in myradiomics. This requires the installation of pyradiomics library.
The data should be in .mat format with:
-First matrix reprensts the image
-Second matrix represents the mask
-The pixel spacing should be stored in px_size variable.

The code will read the images and masks and return the computed radiomic features. The code will loop over all images and return all radiomic features per image. Then, the radiomic features are summarized using the mean value

The next step is to run Data_Analysis.py to check the correlation between the features and keep only the non-correlated ones. 

Run Clustering.R to determine the number of clusters. The code runs consensus clustering to determine the optimal number of clusters. An alternative implementation in python is provided under Consensus_clustering_python folder.

Once the number of clsuters is determined, run Hierarchical_clustering.py to create the clusters.

Run then Calculate_medoid to determine a single representative feature per cluster.

Finally, run Logisticregression.py to create logistic regression models.

![Central illustration](https://github.com/HMS-CardiacMR/NICM_ICD_Radiomics/assets/9512423/b500a438-fbe0-41aa-9ea3-fc44acb49216)


## Abstract

Background: Risk stratification in patients with non-ischemic cardiomyopathy (NICM) remains challenging. Although late gadolinium enhancement (LGE) CMR is recognized as a major risk factor for VT/VF, the prognostic value of LGE radiomics is unknown.
Objective: To investigate the incremental value of LGE radiomics in improving VT/VF risk assessment in NICM receiving ICD for primary prevention.


Methods: The study cohorts consist of 270 NICM patients (61% male, 58±13 years) from Cleveland Clinic (CCF) for model development and 151 NICM patients (74% male, 53±14 years) from Beth Israel Deaconess Medical Center (BIDMC) for external validation. CMR was performed before ICD implantation for primary prevention. Imaging protocol included cine and LGE. The primary outcome was appropriate ICD intervention defined as shock or anti-tachycardia pacing for VT/VF. From LGE images, we extracted 1005 textural radiomic features from the myocardium (Fig 1). We applied consensus clustering to identify distinct radiomic groups. We then identified a single representative feature per group by calculating the pairwise correlation between the features. To assess the prognostic value of LGE radiomics, we built 2 logistic regression models using CCF data (i) Model 1, including clinical risk factors and scar burden (Fig 1) and (ii) Model 2, which combines Model 1 and LGE radiomics. C-statistics (or AUC) was used to evaluate the prognostic value of the different models. DeLong test was used to compare AUCs.


Results: VT/VF occurred in 40 CCF and 24 BIDMC patients over a follow-up period of 1677±1012 and 1176±960 days, respectively. 

Consensus clustering revealed 3 distinct radiomic groups. Model 2 showed significantly higher AUC than Model 1 (0.71 vs 0.61; p=0.045 in CCF and 0.71 vs 0.60; p=0.018 in BIDMC). 
Conclusions: Radiomic analysis of LGE images provides additional prognostic value beyond LGE burden in predicting arrhythmia in primary prevention NICM. 


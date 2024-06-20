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


![Upload_to_github](https://github.com/HMS-CardiacMR/NICM_ICD_Radiomics/assets/9512423/f543f2ec-09ad-4943-8849-0db9482b986a)


## Abstract

Background: Risk stratification in patients with non-ischemic cardiomyopathy (NICM) remains challenging. Although late gadolinium enhancement (LGE) cardiovascular magnetic resonance (CMR) is recognized as a major risk factor for ventricular tachycardia/ventricular fibrillation (VT/VF), the prognostic value of LGE radiomics is unknown.

Objective: To investigate the incremental value of LGE radiomics in improving VT/VF risk assessment in NICM receiving implantable cardioverter defibrillator (ICD) for primary prevention.

Methods: The study included 270 NICM patients (61% male, 58±13 years) from the Cleveland Clinic Foundation for model development and 113 NICM patients (71% male, 55±14 years) from Beth Israel Deaconess Medical Center for external validation. CMR was performed before ICD implantation for primary prevention. Left ventricular myocardial radiomic features were extracted from LGE images. The primary outcome was appropriate ICD intervention defined as shock or anti-tachycardia pacing for VT/VF. Consensus clustering and pairwise correlation were used to identify the radiomic signature. To assess the prognostic value of LGE radiomics, we built 2 logistic regression models using the development data: (i) Model 1, including clinical risk factors and scar presence, and (ii) Model 2, which combines Model 1 and LGE radiomics. 


Results: VT/VF occurred in 40 (15%) patients in development and 16 (15%) in external validation cohorts over a mean follow-up period of 4.4 and 2.9 years, respectively. Consensus clustering and pairwise correlation revealed three distinct radiomic features. Model 2 showed a higher C-statistic than Model 1 (0.71 [CI: 0.62-0.80] vs. 0.61 [CI: 0.53-0.71]; p=0.028 in development and 0.70 [CI: 0.59-0.85] vs. 0.61 [CI: 0.46-0.77]; p=0.025 in external validation). This also significantly improved risk stratification with a continuous net reclassification index of 0.60 [CI: 0.29-0.91; p<0.001] in development and of 0.29 [CI: 0.26-0.56; p=0.03] in external validation. Additionally, one radiomic feature, namely the gray level co-occurrence matrix autocorrelation, was an independent predictor of VT/VF in both development (HR = 1.45 [95%CI: 1.10-1.91]; p=0.01) and in external validation (HR = 2.38 [95%CI: 1.28-4.42]; p=0.01).

Conclusions: Radiomic analysis of LGE images provides additional prognostic value beyond LGE presence in predicting arrhythmia in NICM patients with primary prevention ICD. 


import scipy.io as sio
import numpy as np
import os
import matplotlib.pyplot as plt
from myradiomics.radiomics_utilities import extract_all_radiomics_features, summarize_radiomics
import pandas as pd


data_dir = 'Data/Data_mat/'
pat_list = os.listdir(data_dir)

volume_width = 128
volume_height = 128

radiomics_params = {}
radiomics_params['binWidth'] = 1
csvfn = "path_to_save_file"
feats = pd.DataFrame()

def save_figures(path, im, mask, index):

    ROI = im + mask
    f, axarr = plt.subplots(1, 3)
    axarr[0].imshow(im, cmap="gray")
    axarr[0].axis("off")
    axarr[1].imshow(mask, cmap="gray")
    axarr[1].axis("off")
    axarr[2].imshow(ROI, cmap="gray")
    axarr[2].axis("off")
    plt.savefig(path + index + ".png")
    plt.close()

i = 0
for idx, pat_dn in enumerate(pat_list):
    print("Started processing patient: ", pat_dn)
    flist = os.listdir(data_dir + pat_dn)
    path_to_save = "Visualization/"+pat_dn+"/"
    if(not os.path.exists(path_to_save)):
        os.makedirs(path_to_save)
    # i = 1
    # index = 1
    for element in flist:
        try:
            mat_fn = data_dir + pat_dn + "/" + element
            data = sio.loadmat(mat_fn)
            data = sio.loadmat(mat_fn)
            image_n_mask = data.get("image_n_mask")
            pxsize = data['px_size'][0]

            image = image_n_mask[:, :, 0]
            # norm_min = np.min(image)
            # norm_max = np.max(image)
            # image = (image - norm_min) / ((norm_max - norm_min) + 0.0001)

            mask = image_n_mask[:, :, 1]

            # save_figures(path_to_save, image, mask, str(index))
            # index += 1

            patient_rad_feats = extract_all_radiomics_features(all_img=image, all_mask=mask,
                                                               voxelspacing=np.asarray([1., 1., 1.]),
                                                               params=radiomics_params,
                                                               manualnormalize=True)  # Jan 24, 2022: True
            #
            SR1 = pd.Series(patient_rad_feats, name=i)
            SR2 = pd.Series([pat_dn], name=i)
            SR = pd.concat([SR2, SR1], ignore_index=True)
            SRDF = pd.DataFrame(SR).transpose()
            feats = feats.append(SRDF, verify_integrity=True)
            feats.to_csv(csvfn, index=False)
            i += 1

        except:
            print("Issue with patient: ", pat_dn, "slice: ", element)


    print('Done saving patient ', pat_dn)

feats.rename(columns={0: 'pat_id'}, inplace=True)
feats.to_csv(csvfn, index=False)
print(feats.head(3))
del feats
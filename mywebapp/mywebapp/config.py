import os
classification_mode = 2 # 1 for DTW Class 2 for Random Forest Class
name_of_area = 'Lampung'
username ='didok49'
password = 'sentinel49'
geojson = '/geo/geojson/Lampung_extent_1.geojson' # make a new function to list geojson file
platformname = 'Sentinel-1'
producttype='GRD'
orbitdirection='Descending'
url = 'https://scihub.copernicus.eu/apihub/'

# Directory to save downloaded sentinel File
sentineldirpath = "//sentineldata//"

# Directory of Praprocessing, Subset and Stack file using snappy
snappy_ops = "/data_input/snappy/operators.txt"
snappy_ops2 = "/data_input/snappy/operators2.txt"
snappy_params = "/data_input/snappy/parameters/"

# Directory of Praprocessing, Subset and Stack file using GPT- *.xml
xmlpath="/data_input/xml/praprocess_xml/"
xmlpathsubset = "/data_input/xml/subset_xml/"
xmlpathstack = "/data_input/xml/stack_xml/"
xmlprocesspath = '/data_output/Temp_file/XMLprocess/'
xmlprocesspathsubset = "/data_output/Temp_file/XMLprocess/"
xmlprocesspathstack = "/data_output/Temp_file/XMLprocess/"
xmlpraprocessresultsubset="/data_output/Temp_file/subset_praproses_result/"
xmlpraprocessresultstack="/data_output/Subset_Stack_result/"

# Directory of Output Prprocess, subset-stack
praprocess_result="/data_output/Praproses_result/"
subset_stack_result = "/data_output/Subset_Stack_result/"
target_name = name_of_area + "_S1A_RF_2018Anual_Medium"

########################################################################################################
# for DTW Time Series classification
log_file_dtw = "/logfile/DTW_logfile/"
start_date = '20180401'
end_date='20181227'
param_dtw = "/data_input/dtw_timeseries/DTW_parameter.txt"
mat_files = "/data_input/dtw_timeseries/mat_files/"
mask_files = "/data_input/dtw_timeseries/landcover_mask/"
dtw_mat_save_dir = "/data_output/dtw_timeseries/result_mat/"
dtw_tif_save_dir = "/data_output/dtw_timeseries/result_tif/"
dtw_save_name = "crop_DTWMap"
########################################################################################################

########################################################################################################
# for Random Forest classification
log_file_rf = "/logfile/RF_logfile/"
rf_date = '20181227'
train_path ="/data_input/random_forest/mat_files/train_mat.mat"
rf_mat_save_dir = "/data_output/random_forest/result_mat/"
rf_tif_save_dir = "/data_output/random_forest/result_tif/"
rf_save_name = "growth_RFMap"
########################################################################################################

# Update Date
try:
    file = open(os.getcwd()+"/update_config/update_date.txt", "r")
    get_date = file.readlines()
    new_start_date = get_date[0].strip()
    new_end_date = get_date[1].strip()
    file.close()
except:pass

# Update folder praprocess
try:
    file = open(os.getcwd()+"/update_config/update_praprocess.txt", "r")
    get_fldr = file.readlines()
    new_folder = get_fldr[0].strip()
    new_praprocessresult = praprocess_result + new_folder +'/'
    file.close()
except:
    pass
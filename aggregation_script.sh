set -e

OUTPUT_DIR="seventh_export_11am_dec_12"
CLASSIFICATION_FILE="${OUTPUT_DIR}/cosmic-shambles-supernova-hunt-classifications.csv"
EXTRATION_FILE="${OUTPUT_DIR}/question_extractor_${OUTPUT_DIR}.csv"
REDUCTION_FILE="${OUTPUT_DIR}/question_reducer_${OUTPUT_DIR}.csv"

panoptes_aggregation extract ${CLASSIFICATION_FILE} extractor_config.yaml -o ${OUTPUT_DIR} -d ${OUTPUT_DIR}
panoptes_aggregation reduce ${EXTRATION_FILE} reducer_config.yaml -o ${OUTPUT_DIR} -d ${OUTPUT_DIR} -F first -c 3
python make_output_csv.py ${REDUCTION_FILE} 0.5

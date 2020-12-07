set -e

OUTPUT_DIR="first_export"
CLASSIFICATION_FILE="${OUTPUT_DIR}/<name of csv file>"
EXTRATION_FILE="${OUTPUT_DIR}/question_extractor_${OUTPUT_DIR}.csv"
REDUCTION_FILE="${OUTPUT_DIR}/question_reducer_${OUTPUT_DIR}.csv"

panoptes_aggregation extract ${CLASSIFICATION_FILE} extractor_config.yaml -o ${OUTPUT_DIR} -d ${OUTPUT_DIR}
panoptes_aggregation reduce ${EXTRATION_FILE} reducer_config.yaml -o ${OUTPUT_DIR} -d ${OUTPUT_DIR} -F first -c 3
python make_output_csv.py ${REDUCTION_FILE} 2

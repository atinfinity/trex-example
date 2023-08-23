import json
from parse_trtexec_log import parse_build_log


def generate_build_metadata(log_file: str, output_json: str):
    """Parse trtexec engine build log file and write to a JSON file"""
    build_metadata = parse_build_log(log_file)
    with open(output_json, 'w') as fout:
        json.dump(build_metadata , fout)
        print(f"Engine building metadata: generated output file {output_json}")


engine_path = "model_bn.onnx.engine"
build_log_fname = f"{engine_path}.build.log"
build_md_json_fname = f"{engine_path}.build.metadata.json"
generate_build_metadata(build_log_fname, build_md_json_fname)

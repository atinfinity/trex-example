import json
from parse_trtexec_log import parse_profiling_log


def generate_profiling_metadata(log_file: str, output_json: str):
    """Parse trtexec profiling session log file and write to a JSON file"""
    profiling_metadata = parse_profiling_log(log_file)
    with open(output_json, 'w') as fout:
        json.dump(profiling_metadata , fout)
        print(f"Profiling metadata: generated output file {output_json}")


engine_path = "model_bn.onnx.engine"
profile_log_file = f"{engine_path}.profile.log"
profile_md_json_fname = f"{engine_path}.profile.metadata.json"
generate_profiling_metadata(profile_log_file, profile_md_json_fname)

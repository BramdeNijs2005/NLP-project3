# Adapted from DL1 course

import argparse
import os


def available_cpus() -> int:
    """Number of CPUs this process may use, on any OS."""
    if hasattr(os, "sched_getaffinity"):
        return len(os.sched_getaffinity(0))
    return os.cpu_count() or 1


def get_config() -> argparse.Namespace:
    """Parse and return the training configuration."""
    parser = argparse.ArgumentParser()  # Parse training configuration

    parser.add_argument(
        "--data_location",
        type=str,
        defaults="./data/preprocessed_data"
    )
    #example
    # parser.add_argument(
    #     "--generate_batch_size",
    #     type=int,
    #     default=5,
    #     help="Batch size for generated sentences in callback",
    # )
    args, _ = parser.parse_known_args()  # Parse known args and ignore the rest
    return args
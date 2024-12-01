def aoc_run(
    full_file_name,
    example_file_name,
    solution_func,
    expected_example_answer
):
    
    def _file_to_list(file_path):
        with open(file_path) as f:
            return [x.replace("\n", "") for x in f.readlines()]

    _ex = solution_func(_file_to_list(example_file_name))
    try:
        assert _ex == expected_example_answer
    except AssertionError as err:
        print(_ex)
        raise err

    print(solution_func(_file_to_list(full_file_name)))
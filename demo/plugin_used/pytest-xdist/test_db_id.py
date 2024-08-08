def test_database_interaction(create_unique_database):
    # 使用 testrun_uid 来确保数据库操作的唯一性
    assert create_unique_database == "111"


def test_file_generation(create_unique_database):
    # 使用 testrun_uid 来确保生成的文件名唯一
    assert create_unique_database == "222"

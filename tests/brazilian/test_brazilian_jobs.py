from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    br_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    print('<<<<<<<<<<<<<<<<,', br_jobs)
    assert br_jobs
    assert br_jobs[0]["title"]
    assert br_jobs[1]["salary"]
    assert br_jobs[2]["type"]
    assert br_jobs[0]["title"] == "Maquinista"
    assert br_jobs[1]["salary"] == "3000"
    assert br_jobs[2]["type"] == "full time"

# Dataset inspection notes

These are the first observations from the uploaded files.

## Dataset 1 — all_job_post.csv
- 1,167 rows
- 5 columns: `job_id`, `category`, `job_title`, `job_description`, `job_skill_set`
- 5 broad categories: HR, INFORMATION-TECHNOLOGY, BUSINESS-DEVELOPMENT, FINANCE, SALES
- 723 unique job titles
- `job_skill_set` contains list-like skill values and is useful for extracting job-market skill requirements.

## Dataset 2 — Skill_Job_Matching_Dataset.csv
- 2,809 rows
- 22 columns
- 6 vocational programs
- 6 job titles
- `Job_Match` is a binary target (0/1)
- `Skill_1` … `Skill_5` are numeric student skill values.
- `Required_Skill_1` … `Required_Skill_5` are numeric requirement values/IDs, not readable skill names.

## Important design decision
Dataset 2 is useful for demonstrating supervised job-match prediction, but it does not directly provide the 25–30 modern tech careers we want in the final Skill Gap Predictor.

Dataset 1 is useful for mining real job titles and skills, especially for the IT category. We will therefore use the datasets for complementary purposes rather than pretending they are directly mergeable.

The next phase should create a normalized skill vocabulary and career mapping, then design the final ML target.

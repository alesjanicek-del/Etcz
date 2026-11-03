---
title: Grading methods
source: https://demo.exam-test.cz/napoveda/admin-organizace/zpusoby-hodnoceni
translation: unofficial-draft
---

Preset rules that decide whether a test taker has passed. Percentage, points, grade bands or mandatory questions.

A grading method decides whether a test taker has passed. The organisation administrator sets up grading methods. Instructors choose one in the test settings. An instructor can also set custom grading for a test.

## New grading method

Open **Administration** → **Grading methods** → **New grading method**.

- **Name**, for example “ZOZ – 80%”.
- **Grading type**:
  - **Percentage correct with threshold**: test takers pass if they reach at least the set percentage of points,
  - **Points with threshold**: test takers pass if they score at least the set number of points,
  - **Grades by band**: the test taker gets a grade based on their percentage. They pass with the set lowest passing grade or better,
  - **All mandatory questions correct and % threshold**: besides the percentage, every mandatory question must be answered correctly.
- **Pass mark (%)** or **Pass mark (points)**.
- **Grade bands**: one per line, with the minimum percentage, a space and the grade, for example `90 1`, `75 2`, `50 3`, `0 4`. Bands must start at 0%. Then set the **Lowest passing grade**.
- **Partial points for questions with several correct answers**. If you leave this unticked, such a question counts as correct only for an exact match.
- **Organisation’s default grading method**: pre-filled for new tests. Only one method can be the default.

If no grading method is selected, the pass mark is 80%.

## Deleting and archiving

In the **Grading methods** overview, the **Used** column shows how many tests use each method.

- You can **Delete** only a grading method that no test uses.
- Archive a method that is in use with **Archive**. It is then no longer offered for new tests or as the default. Tests that use it keep grading as before. Archived methods are in the collapsed **Archived grading methods** section. Click **Restore** to offer a method again.

Deleting, archiving and restoring are recorded in the change log.

## How the result is calculated

The score is the points gained as a percentage of the test’s maximum points. Section weights are included. It is shown to one decimal place. Example: a test has 10 questions worth 1 point each and a pass mark of 80%. A test taker answers 7 questions correctly and scores 7 out of 10 points. Their score is 70%, so they have not passed. They needed at least 8 points to pass.

The test taker’s result, the result details for the instructor and the PDF result report all show the same information. They show the **Grading rule** (with the pass mark converted to points) and **How the result was calculated** (points, score, Passed or Not passed). For a test that was not passed, they also show the **Reason for not passing**. The rule is taken from the attempt record. Later changes to the grading method do not affect attempts already submitted.

*For roles: Organisation administrator*

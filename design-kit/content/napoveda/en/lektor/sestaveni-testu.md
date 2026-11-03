---
title: Building a test step by step
source: https://demo.exam-test.cz/napoveda/lektor/sestaveni-testu
translation: unofficial-draft
---

The Basics → Sections → Parameters → Check wizard. Mandatory and randomly picked questions, tags, time, password, grading and official mode.

Open **Tests and exams → Tests → New test**. The wizard has four steps: **Basics**, **Sections**, **Parameters** and **Check**.

## Step 1: Basics

- **Test name**,
- **Description**: only for you and your colleagues. Test takers do not see it,
- **Start page**: instructions that test takers see before they start.

The test is created in your active branch. Continue with **Create test and continue**.

## Step 2: Sections

Each section picks questions from one question bank. A test can have several sections, for example “Radiation protection” and “Health and safety”.

1. Under **Add section**, choose a **Question bank** and, if you like, a **Section heading**. Then select **Add section**. You only see the banks you are allowed to use in tests.
2. On the section, select **Edit section** and set:
   - **Section weight in grading**,
   - **Pick at random: at least** and **Pick at random: at most**: how many questions are drawn on top of the mandatory ones. The same number in both fields means a fixed number,
   - **Mandatory and excluded questions**: tick **Mandatory** (every test taker gets it) or **Exclude** (it is never picked). The **Filter questions** field only narrows the list,
   - **Allowed tags**: questions are drawn only from those with these tags. **Question must have** sets whether one of the allowed tags is enough or all are needed,
   - **Blocked tags**: questions with these tags are never drawn.
3. The **Section summary** at the top is recalculated after every change: **Mandatory**, **Eligible**, **Picked at random** and **Possible selections**. If there are not enough questions, you see an explanation of the error.
4. Save with **Save section** or **Save and stay**.

Change the order of sections with the ↑ ↓ arrows. Remove a section with **Remove**. While the test has errors, the **Check** step is locked.

## Step 3: Parameters

Parameters are prefilled from the organisation settings.

Once test takers have taken the test for real, some parameters are locked. You can no longer change the time limit, number of attempts, results display, feedback, grading method or official mode. You can still change the password, question display, certificate and training record, and exam monitoring. To change other parameters, use a copy of the test (**Copy test**).

### Test flow

- **Time limit (minutes)**: leave empty for no limit,
- **Shuffle question order**,
- **Question display**: one question per page, or all on one page.

### Access and retakes

- **Test password**: optional,
- **Maximum attempts**: leave empty for unlimited,
- **Allow another attempt only if not passed**.

### Results and feedback

- **Results visible to test taker**: nothing (submission confirmation only), the result, the result and incorrectly answered questions, or a full evaluation with the correct answers,
- **Show result only after the instructor releases it**,
- **Answer feedback**: do not show, after the test is evaluated, or straight after each answer is confirmed (practice tests).

### Grading method

Choose one of the organisation’s preset grading methods, or **Custom grading for this test** (type, threshold, grade bands and partial points). The custom grading fields appear once you choose **Custom grading for this test**. If you choose nothing, the pass mark is 80%. See [Grading methods](../admin-organizace/zpusoby-hodnoceni.md).

### Official mode

**Official test**: test takers get no feedback and no correct answers. A maximum number of attempts is required, and the test cannot be assigned by link. Always turn it on for special professional competence exams. An official test does not issue certificates.

### Certificate and training record

**Issue certificate on pass** with a validity period in months, **Training name**, **Trainer**, **Require trainee confirmation** and **Training syllabus**. See [Certificates and training records](osvedceni-a-zaznam-o-skoleni.md) for details.

Save with **Save and go to check**.

## Step 4: Check

The check summarises the sections and parameters, the total number of questions and **Possible unique test versions**.

Unique test versions differ in question selection, question order (if question shuffling is on) or answer order (if answer shuffling is on). Print and online exams count them the same way. A selection of questions that nobody has had yet comes first. Then comes a new question order, and finally a new answer order. Trial runs do not count. When all combinations have been used, online exams continue with the least used combination. Printing is never refused: extra test versions repeat the least used combinations, and the batch and answer key say so clearly.

In **Expected number of attempts**, enter how many people you expect and select **Recalculate**. If there are too few test versions, the application suggests how to widen the selection.

At the end are the buttons **Preview test version**, **Start trial run**, **Assign test** and **Done**.

## Test list

**Tests** has the tabs **Active**, **Archived** and **Deleted items**, and the filters **Search by name**, **My tests only** and **Branch**. The **Check** column shows “OK” or the number of errors.

Each test has the buttons **Assign** and **Edit** (**Preview** if you have read permission). More actions are in the **More** menu: **Preview**, **Start trial run**, **Copy**, **Permissions**, **Archive** and **Move to Deleted items**. Bring back an archived test with **Restore from archive**, and a deleted test with **Restore**. A test that has been assigned cannot be deleted, only archived.

Can’t see the **New test** button? Your organisation does not allow instructors to create tests. Ask your administrator.

## Test permissions

The test owner grants permissions: on the test, select **Permissions**. You can grant a permission to a user, a branch or the whole organisation:

- **Read**: preview and assign the test,
- **Edit**: change sections and parameters,
- **Owner**: everything, including permissions and transferring ownership.

*For roles: Instructor, Branch administrator, Organisation administrator*

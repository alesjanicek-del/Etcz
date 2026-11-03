---
title: How a professional competence exam works, step by step
source: https://demo.exam-test.cz/napoveda/lektor/zkouska-zoz
translation: unofficial-draft
---

The whole special professional competence exam, from preparing questions to the result report, verification and archiving. In the room, with codes or on paper.

This chapter describes the recommended process for a special professional competence exam (ZOZ). In the application, a candidate is a **test taker**. The linked chapters describe each step in detail.

## 1. Preparing questions (question author)

1. Questions are kept in question banks by topic, for example “Radiation protection” (see [Question banks](../autor/soubory-otazek.md)).
2. Images have a description, and formulas have text for screen readers (see [Editor, images and accessibility](../autor/editor-a-pristupnost.md)).
3. If approval is turned on, an approver approves the questions. Only the approved version goes into the exam (see [Question approval](../autor/schvalovani-otazek.md)).

## 2. Building the test (instructor)

1. Build the test from sections by topic, with mandatory and randomly picked questions (see [Building a test](sestaveni-testu.md)).
2. In the parameters, turn on **Official test**. Test takers then cannot see the correct answers, and a maximum number of attempts is required.
3. Choose a grading method, for example “ZOZ – 80%” (see [Grading methods](../admin-organizace/zpusoby-hodnoceni.md)).
4. In the **Check** step, enter the expected number of candidates. Make sure there are enough unique test versions.
5. Go through the test yourself with **Start trial run**.

## 3. Exam date

Record the date in the exam calendar (see [Exam calendar](kalendar-zkousek.md)). The application is not updated during the exam.

Candidates with a disability ask for extra time in advance. You set it on their code or account.

## 4a. Exam in the room on computers or phones (supervised in-room exam)

1. Create a **Supervised in-room exam** assignment and open **Projector screen ↗** on the projector (see [Supervised in-room exam](prezencni-zkouska.md)).
2. Candidates join with the QR code and enter their name. Check the list in the waiting room and remove anyone who should not be there.
3. Select **Lock entry and start test**.
4. Follow progress in the live monitor. If there are problems, extend the time or allow handover to another device (see [Extending time, handover and ending an attempt](prodlouzeni-prevzeti-ukonceni.md)).

## 4b. Exam with personal access codes

1. Create a **Personal access codes** assignment with the candidates’ names (see [Ways to assign a test](zpusoby-zadani-testu.md)).
2. The code table is shown only once. Print it straight away and cut it up.
3. Each candidate enters their code on the `/kod` page.

## 4c. Paper exam

1. Create a print batch. Base the number of test versions on the number of candidates, plus a reserve (see [Printing paper test versions](tisk.md)).
2. Print the question papers and answer sheets. Keep the answer keys separately.
3. After the exam, enter the answers from the sheets with **Enter paper answers**.

## 5. Evaluation and result report

1. When the assignment is over, select **Close**.
2. Check the results in **Results**. For each attempt, you can view the activity record (see [Results and result reports](vysledky-a-protokol.md)).
3. Download the **Result report (PDF)** for the file. The result report has a verification code and a QR code.
4. If results are released by the instructor, release the results.

## 6. Verification and archiving

- Anyone can verify that a result report is genuine on the report verification page (see [Verifying a result report](../zkouseni/overeni-protokolu.md)).
- When the retention period ends, test takers’ personal data is anonymised. The result report stays verifiable.
- If you need to keep a record for longer (for example, for an appeal), the organisation administrator can protect it with **Protect record** (see Personal data, anonymisation and data export).

*For roles: Instructor, Branch administrator, Organisation administrator, Customer (authorised representative)*

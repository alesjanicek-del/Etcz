---
title: Exam monitoring
source: https://demo.exam-test.cz/napoveda/lektor/dohled-nad-zkouskou
translation: unofficial-draft
---

Optional light-touch monitoring without a camera: leaving the window is recorded, full screen, copy blocking, fast answers and submission after leaving the window repeatedly.

Exam monitoring records when a test taker leaves the window during the test. Depending on the settings, it can also warn them, or submit the test after they leave the window repeatedly. It is light-touch monitoring: no camera, no microphone, no screen recording and no artificial intelligence. The application does not track the test taker’s other apps or devices.

Events are information for you. They do not automatically mean cheating. The window can also switch because of a system notification, a low battery or an assistive aid. A person always decides what an event means and what happens next.

## Test settings

Open the test → **3. Parameters** → the **Exam monitoring** section. The **Exam monitoring** field has four options:

- **Off** (default): leaving the window is recorded only in the activity log.
- **Record only**: all monitoring events are recorded. The test taker sees no warning.
- **Record and warn test taker**: when the test taker returns to the window, they see the warning “You left the test window. We have recorded this.” The warning does not block anything, and screen readers read it out.
- **Submit after leaving the window repeatedly**: set the number in **Submit after this many times leaving the window** (default 3). The field appears once you choose this mode. When the test taker leaves the window that many times, the test is submitted with the answers saved so far. It is evaluated like a normal submission. The test taker sees a counter, and the result page tells them why the test was submitted.

Additional options (shown and active only when monitoring is on):

- **Offer full screen and record leaving it**: the test taker gets a **Go full screen** button. If they leave full screen, this is recorded and they are offered a way back. Anyone who cannot use full screen (some phones, browsers or assistive aids) takes the test as normal, and nothing is recorded for them.
- **Block copying question text and pasting into answers**: blocks only copying of questions and answers. Selecting text, zooming and screen readers are not restricted. Copying is recorded even without blocking.
- **Unusually fast answer (seconds)**: records the first answer to a question if it arrives before the set number of seconds since the question was shown. Leave empty to turn this off. The application measures the time, not the test taker’s device.

A change to the settings applies to attempts started after you save. Attempts in progress and submitted attempts keep the settings from when they started. You can change monitoring even on a test that has already been used for a real exam.

Each type of event is recorded at most a few times a minute. This stops a stuck key or repeated switching from flooding the record.

## Official test

For an official test, only certain administrators can turn on **Submit after leaving the window repeatedly**. This means an organisation administrator or an administrator of the test’s branch. By saving the settings, they approve this mode. Their name and the approval time are shown on the test and recorded in the change log. If someone else later changes the mode or the number, the approval is cancelled and the test cannot be saved. A copy of an official test does not inherit the approval. Until an administrator approves it, test takers are only warned.

## What the test taker knows in advance

Before starting, the test taker sees on the test start page that monitoring is on, what is recorded and when the test submits itself. The privacy information for test takers has an “Exam monitoring” section.

During the test, a permanent monitoring notice is shown above the questions, with the link **About monitoring and data processing**. This link and the footer links (privacy information, accessibility statement) open in a window on the test page itself. So reading them does not count as leaving the window.

Extra time for test takers with a disability works with monitoring too. Some aids take over the window, for example dictation, a separate magnifier, or some screen readers and voice control. If a test taker uses one, set an exemption for them (see below). Automatic submission could submit their test against their will and put them at a disadvantage because of their disability. It is enough to know about the aid. Do not ask for a diagnosis.

## Monitoring exemption for one test taker

Open the test assignment (access codes, group assignment or supervised in-room exam) → **Monitoring exemptions**. Choose the test taker and select a mode. **Record only** turns off warnings, automatic submission, full screen and copy blocking, but you still see the events. **No monitoring** works like a test without monitoring. Finally, enter a reason without a diagnosis, for example “assistive technology”. For a supervised in-room exam, set the exemption for the participant in the waiting room before you let them in.

The exemption applies to attempts the test taker starts after you save. An attempt in progress does not change. The attempt record (and result report) only states that an exemption applied and in which mode. The reason is kept only on the assignment and in the change log. You can cancel an exemption. The cancellation is also recorded in the change log. In the live monitor, an attempt with an exemption has the badge “Exemption: record only” or “Exemption: no monitoring”.

## Before you turn on monitoring: personal data and proportionality

Your organisation, as the data controller, is responsible for turning on monitoring and for decisions about its consequences (terms of service, Art. 8.3; data processing agreement, Art. 4.3). Recommendations:

- **Turn it on only where it is needed.** For practice tests and routine training, **Off** or **Record only** is usually enough. Keep automatic submission for exams where something depends on the result, and only when you have no other supervision.
- **Employees.** If you test your own employees, tell them in advance what is checked and how (Czech Labour Code, Section 316(3)). The test start page tells every test taker, but you can also mention it in the invitation or in an internal policy.
- **Impact assessment (DPIA).** Before you turn on automatic submission widely, consider a data protection impact assessment (Art. 35 GDPR). This applies especially to public authorities, employees or large numbers of test takers. Talk to your data protection officer. The operator can provide a description of the feature on request.
- **Automatic submission is decided by software, not by a person.** Something may depend on the exam result (a job, a licence, an official exam). Then the test taker must be able to ask for a review by a person (Art. 22 GDPR). The information for test takers says so, but your organisation handles the requests.
- **Your own privacy information text.** The “Exam monitoring” section is shown below your own text too. Its legal basis refers to your text. So mention the technical record of test activity in your text as well.

## When a test taker disputes an automatic submission

A submitted attempt cannot be reopened or changed. So a review means that a person assesses the circumstances and decides whether the result stands. In the result details, an attempt submitted by monitoring has the notice “Submitted by monitoring, awaiting review”. In the live monitor, it has the badge **Awaiting review**.

1. Open the result details and go through the timeline of monitoring events (when and for how long the test taker was outside the window).
2. Hear the test taker out: a technical problem, a system notification, an assistive aid.
3. Under **Exam monitoring → Review submission by monitoring**, choose:
   - **Accept result**: the result stays valid;
   - **Invalidate and allow a replacement attempt**: the attempt is no longer valid. It does not count in results, statistics or exports, and any certificate from it is invalid. The test taker can take the test again with the same code or from **My tests**. The replacement attempt does not count towards the maximum number of attempts. The assignment must still be open at that time.
4. Enter a reason (at least 5 characters, no health information) and save.

You can make only one decision, and you cannot undo it. The reason, name and time are recorded with the result, in the PDF result report and in the change log. The test taker gets an email if their account or access code has an email address. Otherwise, tell them the decision yourself. Public result report verification shows only the status, not the reason or the events. The status is “result accepted” or “attempt invalidated”, with a link to the replacement attempt. The invalidated attempt stays in the unchangeable record. You can find it through the assignment’s live monitor. The replacement attempt links to it.

For an official test, only an organisation administrator or a branch administrator can review a submission by monitoring. Instructors see that the decision belongs to an administrator.

The application does not decide on any further consequences (for example, disciplinary ones). It does not conclude from events that someone cheated.

## Where to see events

- The assignment’s **Live monitor**: in the **Alerts** column, each test taker has a badge with text, for example “Monitoring: 2 events (window 1×, copying 1×)”. A green “Monitoring: no events” badge means nothing happened. Yellow means events below the limit. Red “check” means the limit was reached. A separate “Submitted by monitoring” badge marks an attempt that monitoring submitted. See [Live monitor](zivy-panel.md).
- **Result details**: the **Exam monitoring** section with the mode, a summary and a timeline of events.
- **Result report (PDF)**: an **Exam monitoring** line in the header and a table of monitoring events.
- **Test statistics**: how many attempts have monitoring events, by type, and how many were submitted by monitoring. See [Statistics](statistiky.md).

Events are stored in the unchangeable exam record, like the rest of the test activity. Nobody can delete or change them afterwards.

*For roles: Instructor, Branch administrator, Organisation administrator*

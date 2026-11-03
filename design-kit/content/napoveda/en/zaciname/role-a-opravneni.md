---
title: Roles and permissions
source: https://demo.exam-test.cz/napoveda/zaciname/role-a-opravneni
translation: unofficial-draft
---

# Roles and permissions

What an organisation administrator, branch administrator, instructor, question author, learner and test taker without an account can do.

## Roles

Each user can have several roles, including in different branches. The question author role is usually combined with the instructor role.

| What you can do | Organisation administrator | Branch administrator | Instructor | Question author | Learner | Test taker without an account |
|---|---|---|---|---|---|---|
| Organisation settings, logo, texts, data retention | yes | — | — | — | — | — |
| Branches | creates and edits | sees own | — | — | — | — |
| Users, roles, groups, resetting two-step verification | yes | in own branches (for users, only those in own branches) | — | — | — | — |
| Question banks | all | in own branch and by permission | by permission for the bank | by permission for the bank | — | — |
| Approve questions | yes | only if the organisation allows it | — | — | — | — |
| Tests | all | in own branch and by permission | by permission for the test | — | — | — |
| Use a test (code, link, assigned to a group, supervised in-room exam, print) | yes | in own branch | in own branch, if allowed to read the test | — | — | — |
| Live monitor, extending time, ending an attempt | yes | in own branch | for own test assignments | — | — | — |
| Print batches, answer keys, entering paper answers | yes | own branch’s batches | own branch’s batches | — | — | — |
| Results, result report, export | all | in own branch | for own test assignments | — | own result | own result |
| Statistics | yes | yes | by permission for the bank | by permission for the bank | — | — |
| Change log (audit) | yes | actions of users in own branches | — | — | — | — |
| Allow support technician access | yes | — | — | — | — | — |
| Take a test | — | — | — | — | assigned tests | by code or link |
| Verify a result report | anyone, even without signing in | | | | | |

A branch administrator cannot appoint an organisation administrator.

## Permissions for question banks and tests

As well as your role, your permission for a specific question bank or test also counts:

- **Owner** has full access, grants permissions to others, can move the bank or test to **Deleted items** and transfer ownership.
- **Edit** lets you edit the content and see statistics, and for a question bank, use it in tests.
- **Read** lets you use it in tests (for a test: preview and test assignment) and see statistics, but not change anything.

You can grant a permission to one user, a whole branch or the whole organisation. The organisation administrator has full access to everything.

How to grant permissions is described in [Question banks](../autor/soubory-otazek.md) and [Building a test](../lektor/sestaveni-testu.md).

## Who can do what in branches

- **Instructors** work in the branches where they have a role. They can have several and switch between them with the **Active branch** switcher.
- **Branch administrators** manage the instructors, learners and groups in their branch. They cannot see other branches.
- **Organisation administrators** see all branches and results with no branch.

*For roles: everyone*

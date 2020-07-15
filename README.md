
# My-Fitness-Log

A workout planner and log that I would want to use.

## Project Overview

A workout planner built with [django](https://www.djangoproject.com) that generates custom data tables to fit the users needs and saves them into a database for future reference.

## Functionality

- [ ] display motivational quote of the day
- [x] create user
    - [x] log in
- [ ] select muscle group
    - [ ] choose exercises
    - [ ] generate random workout
    - [ ] provide image of individual workout
    - [ ] log date and time
        - [ ] add set
        - [ ] add reps
            - [ ] log weight being lifted
            - [ ] log user weight
            - [ ] complete workout

## Data Models

**Exercise Model**
- id (IntegerField)
- muscle_group (CharField)
- image_url (CharField)

**User**
- user_name (CharField)

**Workout**
- date_time (DateTimeField)
- set (IntegerField)
- reps (IntegerField)
- user_weight (IntegerField)
- weight_lifted (IntegerField)
- exercise (ManyToManyField)
- user (ForeignKey)

## Scedule

- Week 1
  - [x] create django project
  - [ ] create models
  - [x] user registration
  - [x] user log in
- Week 2
  - [ ] create muscle groups (types)
  - [ ] custom management command to load exercises into database
  - [ ] allow user to make own workout
  - [ ] allow user to add workouts
- Week 3
  - [ ] styling, motivational quote


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
- exercise (ManyToManyField)
- set (IntegerField)
- reps (IntegerField)
- user_weight (IntegerField)
- weight_lifted (IntegerField)
- user (ForeignKey)

## Scedule

- Week 1
  - [x] create django project
- Week 2
  - [x] create user models
  - [x] user registration
  - [x] user log in
  - [x] allow user select muscle groups (types)
- Week 3
  - [x] create workout models
  - [x] allow user to make own workout
  - [ ] allow user to save workouts
  - [ ] styling, motivational quote

# Rocket Launch

## Project Goal

The goal of this project is to help me hone my skills with Python, SQL, pytest, and REST APIs.
Along with learning new skills such as:

- Docker
- Linux
- AWS
- Pandas

## What I am building

Launch dates and launch statuses can change a lot, and APIs usually only show what the latest version of that launch looks like. I want to build a pipeline that can pull launch data, save the original data, clean it up, and eventually use it to look at changes and answer questions about launches.

## My why?

Space is one of those topics that really gets me going. So when considering what my next project should be I couldn't help but make it space themed.
I think this will be a great way for me to learn to handle "enterprise" level data handling/automation while also keeping it something I am interested in.

## Project Roadmap:

I know this project is going to take some time, so I am going to start small and build it up as I learn more.

- First, I want to learn how the Launch Library API works and pull a small amount of launch data from it.
- After that, I want to figure out how to pull more than one page of data and save the original responses so I can work with them later.
- Once I have that part down, I will learn more about PostgreSQL and SQL so I can safely store the launch data without making duplicates.
- From there, I want to add validation, error handling, logging, and a way to understand what went wrong if the pipeline fails.
- I also want to use SQL and Pandas to answer questions about the launch data instead of just storing it.
- Toward the end of the project, I want to learn how to run it with Linux, Docker, and eventually AWS.

## Setup

This project is currently using Python 3.13 and uv for dependency management.

To set up the project environment:

```powershell
uv sync --python 3.13
```

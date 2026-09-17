Day 3: OOP for Pipelines

Objective

Learn how Object-Oriented Programming (OOP) can be used to design
modular and maintainable data processing pipelines.

Topics covered:

Abstract Base Classes

Inheritance

Polymorphism

Composition

Reusable pipeline steps

Unit testing

Project Overview

A customer churn detection pipeline was created using multiple
independent processing steps.

Each step performs one specific task, and the Pipeline class combines
these steps into a complete workflow.

The workflow is:

Input Data
    |
    v
Validation
    |
    v
Remove Missing Values
    |
    v
Feature Engineering
    |
    v
Processed Data

Concepts Implemented

1. Abstract Base Class

The Step class defines a common interface for all pipeline steps.

class Step(ABC):
    @abstractmethod
    def run(self, data):
        pass

Every child class must implement the run() method.

2. Inheritance

The individual pipeline steps inherit from the common Step class.

Examples:

LoadDataStep

ValidateDataStep

RemoveMissingValuesStep

FeatureEngineeringStep

3. Polymorphism

The pipeline calls:

step.run(data)

without needing to know which specific step is being executed.

Each step provides its own implementation of run().

4. Composition

The Pipeline class contains a collection of independent steps.

pipeline = Pipeline(
    [
        ValidateDataStep(),
        RemoveMissingValuesStep(),
        FeatureEngineeringStep(),
    ]
)

This allows steps to be combined, reordered, or replaced easily.

Pipeline Steps

Step                        Responsibility

LoadDataStep              Provides the initial data
ValidateDataStep          Checks required fields
RemoveMissingValuesStep   Removes incomplete records
FeatureEngineeringStep    Creates the customer_value feature

Example Feature

The feature engineering step calculates:

customer_value = tenure × monthly_charges

For example:

tenure = 12
monthly_charges = 65.5

customer_value = 12 × 65.5 = 786.0

Testing

Run the test suite using:

python -m pytest -q

Expected result:

4 passed

Running the Demo

Run:

python -m scripts.demo_pipeline

The demo shows:

Validation and feature engineering.

Missing-value removal followed by feature engineering.

Key Learning Outcome

This task demonstrates how composition can be used to build flexible
pipelines without creating deep inheritance hierarchies. Each processing
step has a single responsibility and can be independently tested and
reused.
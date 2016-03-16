Title: Introducing cesium
Tags: cesium
Status: published
Date: 2016-03-18

## Machine learning for time series
The analysis of time series data is a fundamental part of many scientific disciplines,
including astronomy, bioinformatics, neuroscience, seismology, and many others. Despite the
importance of such analyses, there are few resources available that allow domain scientists to
easily explore time course datasets: traditional statistical models of time series are
often too rigid to explain complex time domain behavior, while popular machine learning
packages deal almost exclusively with 'fixed-width' datasets containing a uniform number of
features. `cesium` allows researchers to apply modern machine learning techniques to time
series data in a way that is both simple and easily reproducible.

## Simplifying the analysis workflow
Building a functioning machine learning pipeline involves much more than choosing a
mathematical model for your data. The goal of `cesium` is to simplify the analysis pipeline so
that scientists can spend less time solving technical computing problems and more time
answering scientific questions. By streamlining the process of fitting models and studying
relationships within datasets, `cesium` allows researchers to iterate rapidly and quickly answer
new questions that arise out of previous lines of inquiry. We also aim to make analyses using
`cesium` easily shareable and reproducible, so that an entire process of discovery can be
shared with and reproduced by other researchers.

## Scaling to large datasets
In many fields, the volumes of time series data available can be immense. `cesium` makes the
process of analyzing time series easily parallelizable and scaleable; scaling an analysis
from a single system to a large cluster should be easy and accessible to non-technical experts.
The analysis workflow of `cesium` can be used in two forms: a web front end which allows
researchers to upload their data, perform analyses, and visualize their models all within the
browser; and a Python library which exposes more flexible interfaces to the same analysis
tools. The code for both the web frontend and Python library are open source and available on
[Github](https://github.com/cesium-ml). In our next post, we'll show how the Python library can
be used to quickly solve a classic EEG classification problem.

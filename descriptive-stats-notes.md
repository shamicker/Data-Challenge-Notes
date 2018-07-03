<!-- TOC -->

- [1. Descriptive Statistics](#1-descriptive-statistics)
    - [1.1. Intro to Research Methods](#11-intro-to-research-methods)
        - [1.1.1. Lesson 1 PDF](#111-lesson-1-pdf)
        - [1.1.2. Constructs](#112-constructs)
        - [1.1.3. Extraneous Factors](#113-extraneous-factors)
        - [1.1.4. Population Parameter](#114-population-parameter)
        - [1.1.5. Sample statistics](#115-sample-statistics)
        - [1.1.6. Correlation does not prove causation!](#116-correlation-does-not-prove-causation)
        - [1.1.7. Observational studies](#117-observational-studies)
        - [1.1.8. Surveys](#118-surveys)
        - [1.1.9. Controlled experiment](#119-controlled-experiment)
        - [1.1.10. Within subject design](#1110-within-subject-design)
        - [1.1.11. Indicator Response](#1111-indicator-response)
    - [1.2. Visualizing Data](#12-visualizing-data)
        - [1.2.1. Lesson 2 PDF](#121-lesson-2-pdf)
        - [1.2.2. Frequency Table](#122-frequency-table)
        - [1.2.3. Relative Frequency](#123-relative-frequency)
        - [1.2.4. Bar Chart](#124-bar-chart)
        - [1.2.5. Bar Graph](#125-bar-graph)
        - [1.2.6. Histogram](#126-histogram)
        - [1.2.7. InterActivate is a *histogram software*](#127-interactivate-is-a-histogram-software)
        - [1.2.8. Normal distribution](#128-normal-distribution)
        - [1.2.9. Positively skewed distribution](#129-positively-skewed-distribution)
    - [1.3. Central Tendency](#13-central-tendency)
        - [1.3.1. Lesson 3 PDF](#131-lesson-3-pdf)
        - [1.3.2. Mode](#132-mode)
        - [1.3.3. Mean](#133-mean)
        - [1.3.4. Median](#134-median)
    - [1.4. Variability](#14-variability)
        - [1.4.1. Lesson 4 PDF](#141-lesson-4-pdf)
        - [1.4.2. Interquartile Range (IQR)](#142-interquartile-range-iqr)
        - [1.4.3. Outliers](#143-outliers)
        - [1.4.4. Boxplots](#144-boxplots)
        - [1.4.5. Deviation (from the *mean*/average)](#145-deviation-from-the-meanaverage)
        - [1.4.6. Squared deviations](#146-squared-deviations)
        - [1.4.7. SS](#147-ss)
        - [1.4.8. variance](#148-variance)
        - [1.4.9. Standard Deviation](#149-standard-deviation)
        - [1.4.10. Bessel's Correction](#1410-bessels-correction)
    - [1.5. Standardizing](#15-standardizing)
        - [1.5.1. Lesson 5 PDF](#151-lesson-5-pdf)
        - [1.5.2. Standardizing](#152-standardizing)
        - [1.5.3. Continuous Distribution](#153-continuous-distribution)
        - [1.5.4. Z](#154-z)
        - [1.5.5. Z-Score](#155-z-score)
        - [1.5.6. Standard Normal Distribution](#156-standard-normal-distribution)
    - [1.6. Normal Distribution](#16-normal-distribution)
        - [1.6.1. Lesson 6 PDF](#161-lesson-6-pdf)
        - [1.6.2. Normal Distribution](#162-normal-distribution)
        - [1.6.3. Probability Density Function (PDF)](#163-probability-density-function-pdf)
    - [1.7. Sampling Distributions](#17-sampling-distributions)
        - [1.7.1. Lesson 7 PDF](#171-lesson-7-pdf)
        - [1.7.2. Samples:](#172-samples)
        - [1.7.3. Sampling Distribution](#173-sampling-distribution)
        - [1.7.4. Expected Value](#174-expected-value)
        - [1.7.5. Standard Error (SE)](#175-standard-error-se)
        - [1.7.6. Central Limit Theorem](#176-central-limit-theorem)
        - [1.7.7. Other Key TakeAways](#177-other-key-takeaways)
- [2. Python](#2-python)
    - [2.1. Control Flow](#21-control-flow)
        - [2.1.1. Zip()](#211-zip)
        - [2.1.2. List Comprehensions](#212-list-comprehensions)
    - [2.2. Functions](#22-functions)
        - [2.2.1. Documentation](#221-documentation)
        - [2.2.2. Lambda Expressions](#222-lambda-expressions)
        - [Map](#map)
        - [Filter](#filter)
        - [Iterators and Generators](#iterators-and-generators)

<!-- /TOC -->
# 1. Descriptive Statistics

## 1.1. Intro to Research Methods

### 1.1.1. Lesson 1 PDF
- [Lesson 1 PDF](Lesson1.pdf)

### 1.1.2. Constructs
- In scientific theory, particularly psychology, a hypothetical construct is an explanatory variable which is not directly observable. (itchiness, happiness, stress, intelligence, motivation, etc)

- measured with an **operational definition**.
- For instance, *happiness* could be measured by the ratio of minutes spent smiling to minutes not smiling. Here, the ratio is the **operational definition** of *happiness*.

### 1.1.3. Extraneous Factors
- aka lurking variables
- things that could influence the outcome, that aren't necessarily considered. (the surprise unknowns)

### 1.1.4. Population Parameter
- denoted by <code>$\mu$</code> (mu)
- are values that describe the ENTIRE population (as an average)

### 1.1.5. Sample statistics
- denoted by <code>$\bar{x}$</code> (x-bar)
- are values that describe a sample (the sample that were tested) (as an average)

We use <code>$\bar{x}$</code> to estimate <code>$\mu$</code>.

**Independent** or the **predictor** variable - the x-axis variable

**Dependent** or the **outcome** variable is the y-axis variable

---
---
### 1.1.6. Correlation does not prove causation!
---
---
### 1.1.7. Observational studies
- To show relationships.
- Just ask people and you'll see a trend.

### 1.1.8. Surveys
- a type of observational study
- **response bias** - when respondents don't understand a question
- **non-response bias** - when they refuse to answer a question

### 1.1.9. Controlled experiment
- to show **causation**
- to deal with all the extraneous factors (lurking variables)

### 1.1.10. Within subject design
- controlling for variation within a person.
- For example, testing after different amounts of sleep. You're controlling the variation in people's individual memory capabilities, depending on the amounts of sleep they got.

### 1.1.11. Indicator Response
- ex. Pouched rats scratching near tea eggs containing TNT. So I guess it's *indicating* that TNT is nearby. The humans needed some kind of **indicator response** from the mice to know when there was TNT nearby.

---

## 1.2. Visualizing Data

### 1.2.1. Lesson 2 PDF
- [Lesson 2 PDF](Lesson2.pdf)

### 1.2.2. Frequency Table
- counts the frequency of each data type (ie, if countries, then each country)
- they are whole numbers, obviously, since it's a count.

### 1.2.3. Relative Frequency
- How much of the whole each data point comprises.
- **Absolute** numbers are whole numbers (12 or 43 out of 50)
    - the sum is the number of data points (<code>$n$</code> or <code>$N$</code>)
- **Proportions** are the fraction written with decimals (.24 or .86)
    - the sum is 1
- **Percentages** are with the <code>%</code> sign (24% or 86%)
    - the sum is 100%

### 1.2.4. Bar Chart
- measures **frequency** of your data, which is grouped into **intervals** or **bins**
- the **intervals** are on the x-axis
- the **frequency** is on the y-axis

### 1.2.5. Bar Graph
- data is grouped **categorically** or **qualitatively**
- can't be grouped (much) differently because the groups are distinct categories
- space between data groupings

### 1.2.6. Histogram
- a type of bar chart
- data is grouped **numerically** or **quantitatively**
- *no* space between data groupings (unless frequency is 0)
- the **intersection of the axes** is (0,0) (Cartesian coordinates)
- can be *biased*! Always look at labels & numbers

### 1.2.7. InterActivate is a *histogram software*

### 1.2.8. Normal distribution
- one large, middle peak called the **mode**; symmetrical

### 1.2.9. Positively skewed distribution
- peak is on the left
- most values on the left

---
## 1.3. Central Tendency

### 1.3.1. Lesson 3 PDF
- [Lesson 3 PDF](Lesson3.pdf)

3 measures of center: mode, median, mean

### 1.3.2. Mode
- most common occurrence - ie, in [1, 2, 3, 4, 4] it's 4
- value at which the *frequency* is highest (the tallest peak)
- can be used for any data - *categorical* or *numerical*
- no actual formula for finding it.

### 1.3.3. Mean
- the **average** of the distribution
- ALL scores in distribution affect the mean
- mean of a sample denoted by <code>$\bar{x}$</code>
- mean of a population denoted by <code>$\mu$</code>
- formula for a sample: <code>$\bar{x} = \frac{\sum x}{n}$</code>
- formula for a population: <code>$\mu = \frac{\sum x}{N}$</code>
- many samples from the same population will have similar means (!!!)
- the mean of a sample can be used to make inferences about the population it came from (!!!)
- **outliers** - outlying data points that completely skew the average
[tough quiz](https://classroom.udacity.com/courses/ud002-bert/lessons/1489118552/concepts/773143370923)

### 1.3.4. Median
- value in the middle of the distribution
- if there are 2 numbers, it's the middle of the middles (the average of the middle 2 numbers)
- **ROBUST** = doesn't change much due to outliers
- best measure of central tendencies when dealing with highly skewed distributions
- formula for an even number of values:
<code>$\frac{x_\frac{n}{2} + x_{\frac{n}{2}+1}}{2}$</code>
- formula for an odd number of values: <code>$x_\frac{n+1}{2}$</code>

---
## 1.4. Variability

### 1.4.1. Lesson 4 PDF
- [Lesson 4 PDF](Lesson4.pdf)

### 1.4.2. Interquartile Range (IQR)
- divide the data into quarters, and subract the lower median from the upper median (Q3 - Q1). This is the IQR.
- roughly 50% of data is within this range
- IQR is **not affected by outliers**.
- more or less describes the spread of the data

### 1.4.3. Outliers
- extreme data points in a distribution
- traditionally cut off top and bottom 25%
- formula to determine outliers: <code>$Outlier < Q_1 - 1.5*(IQR)$</code>
- formula to determine outliers: <code>$Outlier > Q_3 - 1.5*(IQR)$</code>
- traditionally cut off top and bottom 25% of distributions to account for outliers

### 1.4.4. Boxplots
- used to visualize *quartiles* and *outliers*
- outer lines are the *min* and *max* values that are NOT outliers
- the whole box is the *IQR*
- the box edges are, as shown in image below, *Q1*, *Q2*, and *Q3*
- *outliers* are shown as dots outside of the *min* and *max* lines.

![boxplot image](images/boxplot.PNG)

![image](images/match-the-boxplots.PNG)

### 1.4.5. Deviation (from the *mean*/average)
- find the *mean*, then subtract each data point (find the absolute)
- <code>$x_i - \bar{x}$</code> (xi minus x-bar)
- how far from zero it is

### 1.4.6. Squared deviations
- just the *deviations* squared

### 1.4.7. SS
- sum of the squared deviations
- formula: <code>$\Sigma(x_i - \bar{x})^2$</code>

### 1.4.8. variance
- **SS** divided by <code>$n$</code>
- is the average squared deviation
- BUT if we treated the whole as a sample (<code>$n$</code>), it would be divided by (<code>$n - 1$</code>)
    - I don't know why

### 1.4.9. Standard Deviation
- denoted by (small sigma) <code>$\sigma$</code>
- square root of the variance (which is the average of squared deviations)
- the most common measure of spread
- formula: <code>$\sigma=\sqrt{\frac{\Sigma(x_i - \bar{x})^2}{n}}$</code>
- within a *normal distribution*, 68% of data sample falls within a 'standard deviation' from the mean, and 95% of the data sample falls within 2 'standard deviations' from the mean (see figure!).

![point of standard deviation](images/point-of-standard-deviation.PNG)

### 1.4.10. Bessel's Correction
In general, samples under-estimate variability in a population because samples tend to be from the middle (especially in normal distribution).
- To correct for this, *Bessel's Correction*
- get average using <code>$(n-1)$</code> instead of <code>$n$</code>
- use this **ONLY** for approximating populations using samples
- it is **NOT** used for a whole population (or small data set)
- if you've got a sample, where <code>$n = 5$</code> and population is <code>$N = 100$</code>, then use Bessel's Correction.
- denoted by (small s) <code>$s$</code>

**Sample standard deviation** is the standard deviation of a sample (not a population), and it uses *Bessel's Correction* to approximate the population. Its formula is: <code>$s \approx \sqrt{\frac{\Sigma(x_i - \bar{x})^2}{n-1}}$</code>

Variance with Bessel's Correction (for a sample): <code>$\frac{\Sigma(x_i = \bar{x})^2}{n-1}$</code>

---
## 1.5. Standardizing

### 1.5.1. Lesson 5 PDF
- [Lesson 5 PDF](Lesson5.pdf)

### 1.5.2. Standardizing
This term is used to compare 2 different distributions (ie Twitter vs Facebook followers). Basically, we compare them using their standard deviations as the common unit. For example, we would compare how many standard deviations away from the mean (which is our zero starting point) that our Z-value is.
- proportion below or above the mean

### 1.5.3. Continuous Distribution
A theoretical model:
- a theoretically continuous (smooth) distribution that can be described with an equation, which calculates the proportion between ANY 2 points on the x-axis.
- area under the curve should be 1 (same as the sum of all the relative frequencies)

In our theoretical model of a *continuous* and *normal* distribution, the *mean*, *median*, and *mode* are all equal.

### 1.5.4. Z
- Marks a point on the x-axis of a distribution

### 1.5.5. Z-Score
- in a standard distribution, the distance in st.dev's away from mean.
    - to calculate this Z-value in terms of standard deviations away from the mean,
we need to know:
        - the Z value/number
        - the mean
        - the standard deviation
    - and then take the difference (mean minus Z) divided by the stand.dev.
- <code>$Z.Score = \frac{x-\mu}{\sigma}$</code> where <code>$x - \mu$</code> will be positive or negative, depending on whether above or below the *mean*.

### 1.5.6. Standard Normal Distribution
Q: What is the standard deviation of a standardized distribution?

A: The z-score of sigma will be 1:

<code>$Z = \frac{x - \mu}{\sigma} = \frac{\sigma - 0}{\sigma} = 1$</code>

This is called the **Standard Normal Distribution**.

![pic of Standard Normal Distribution](images/standard-normal-distribution.PNG)

---
## 1.6. Normal Distribution

### 1.6.1. Lesson 6 PDF
- [Lesson 6 PDF](Lesson6.pdf)

### 1.6.2. Normal Distribution
- bell curve with peak in the center
- the tails never actually touch the x-axis, they just infinitely approach it
    - because we can never be 100% sure that there isn't a value further than that; theoretically, you can have an infinite values in a population


### 1.6.3. Probability Density Function (PDF)
- the curve of a *normal distribution*
- because the area under the curve is 1
    - so we can get the probability of any number on x-axis (aka %)
- there is an extra-curricular equation for this (via calculus)
    - someone created a table for greater ease!
- the *area under the curve* of a normal distribution == the *probability* of randomly selecting less than x == the *proportion* in the sample/population with scores less than x
    - where x is the xth percentile (or the Z)


<code>$s \approx \sqrt{\frac{\Sigma(x_i - \bar{x})^2}{n-1}}$</code>

<code>$Zscore = \frac{\mu -Z}{\sigma}$</code>, and then look up the *area under the curve* on the chart to get the *probability* of data scores less than *X* (or *Z*)

---
## 1.7. Sampling Distributions

### 1.7.1. Lesson 7 PDF
- [Lesson 7 PDF](Lesson7.pdf)

With a single data point, we can compare that value to the rest of the values with *% less* or *% greater*.
Similarly, if we have a sample, we can compare that sample to the rest of the samples!

### 1.7.2. Samples:
- A sample must represent the characteristics of the population.
    - It needs to be *large enough*,
    -  to *have similar characteristics* to the *whole* population
        - ie, if population has 70% women vs men, then sample must have about the same
        - the sample mean should be similar to the population mean.
            - That's how you can tell if your sample is large enough. (??)

### 1.7.3. Sampling Distribution
- the distribution of samples means is the **sampling distribution**
    - the shape will be a *normal distribution*
    - if we calculate *ALL* the sample means, the mean of these sample means (or, the mean of the *sampling distribution*) will equal the population's mean.
        - <code>if $\mu$ of 100% of sampling distribution, then $\mu = M$</code>

### 1.7.4. Expected Value
- the mean of a population is the *expected value*, even if it's not a possible outcome (as in dice rolls).
- it means we can expect an outcome somewhere around this value.

### 1.7.5. Standard Error (SE)
- the standard deviation of the sampling distribution
- the population standard deviation divided by the square root of n: <code>$SE = \frac{\sigma}{\sqrt{n}}$</code>
- So if you have a population size of 1,

![central limit theorem notes](images/central-limit-theorem-notes.PNG)

### 1.7.6. Central Limit Theorem
- for any population, if you take enough samples, and plot those samples' means, you'll get roughly a normal distribution
- aka the *standard error (SE)*
- So:
    - the distribution of means,
    - where every mean is the mean of a sample of size <code>$n$</code>,
    - has a standard deviation equal to the population standard deviation divided by the square root of <code>$n$</code>.

### 1.7.7. Other Key TakeAways
- the larger the sample size (in a population of samples) (ie. n=2 or n=25),
    - the narrower the histogram/ distribution. Which means:
        - the smaller the *Standard Error*
        - the Z-Score will be bigger for the same data point
        - the less likely to get an outlying data point

---
---

# 2. Python

## 2.1. Control Flow
This is lesson 25. I skipped what was review for me.

### 2.1.1. Zip()
<code>zip</code>
    - returns an iterator
    - combines multiple iterables into a sequence of tuples
        - each tuple contains the elements in that position from all the iterables.

General example:
```
list( zip(['a', 'b', 'c'], [1, 2, 3]) )
```
outputs
```
[('a', 1), ('b', 2), ('c', 3)]
```

Example using `for` loop:

```
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print( "{}: {}".format(letter, num) )
```

`zip` also works in reverse (unzipping).
Example:
```
some_list = [('a', 1), ('b', 2), ('c', 3)]

letters, nums = zip(*some_list)
```

### 2.1.2. List Comprehensions
These is sort of a shortcut. It allows us to create a list using a `for` loop in a single step!
- not found in any other language, but very common in Python. :)

```
capitalized_cities = []
for city in cities:
    capitalized_cities.append( city.title() )
```

can be reduced to:
```
capitalized_cities = [city.title() for city in cities]
```

Used with conditionals:
```
squares = [x**2 for x in range(9) if x % 2 == 0]
```

With an `else`:
```
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
```

## 2.2. Functions

### 2.2.1. Documentation
```
def population_density(population, land_area):
    """Calculate the population density of an area.
    INPUT:
    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic,
    if you pass in values in terms of square km or square miles
    the function will return a density in those units.
    OUTPUT:
    population_density: population/land_area.
    The population density of a particular area.
    """
    return population / land_area
```

### 2.2.2. Lambda Expressions
Used to create quick, "throw-away" anonymous functions.
```
def multiply(x, y):
    return x * y
```
can be reduced to:
```
multiply = lambda x, y: x * y
```

### Map
`map` takes in a `function` and an `iterable` as inputs, and returns an interator that applies the function to each element of the iterable.

```
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]


def mean(list):
    return sum(list) / len(list)

averages = list(map(mean, numbers))
print(averages)
```
With `lambda`:
```
averages = list(map(lambda x: sum(x) / len(x), numbers))
```

### Filter
`filter` takes a `function` and `iterable` as inputs, just like `map`, and returns an iterator with the elements from the iterable *for which the function returns `True`*.
```
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)
```
With `lambda`:
```
short_cities = list(filter(lambda x: len(x) < 10))
```

### Iterators and Generators

*Iterables* are objects that can return one of their elements at a time, such as a list. Mny of the built-in functions we've used so far, like `enumerate`, return an iterator.

An *iterator* is an object that represents a *stream of data*. This is different from a list, which is also an iterable, but not an iterator because it is not a stream of data.

*Generators* are a simple way to create iterators using functions. You can also define iterators using *classes*.

Why would we use them rather than a list? Here's an excerpt [from stack overflow](https://softwareengineering.stackexchange.com/questions/290231/when-should-i-use-a-generator-and-when-a-list-in-python/290235):

    Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.



Example of a generator function called `my_range`, which produces an iterator that is a stream of numbers from 0 to (x-1).
```
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
```
Notice that is uses `yield`. This allows the function to return values, but to continue on.
- This `yield` keyword is what differentiates a generator from a typical function.


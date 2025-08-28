# Matrix Clusters

A Python package to detect and count **clusters of connected cells** in two-dimensional (2D) and three-dimensional (3D) matrices.  

It supports both **binary matrices** (0s and 1s) and **continuous matrices**, applying a configurable threshold (`threshold`) to decide which values belong to a cluster.

---

## Introduction

Clustering algorithms are methods used to group vectors according to a given criterion. This criterion, as in the case of the algorithm described here, can be based on **distance or neighborhood connectivity**, allowing classification into groups called clusters.  

In this project, clustering is applied to **2D and 3D matrices**, which are commonly found in many fields of research such as physics and mathematics. The package works with both **binary matrices** and **continuous matrices**.

A **binary matrix** is simply a table of values made up of 0s and 1s.  
- The value **1** typically represents the presence of something (e.g., a white pixel, an active node).  
- The value **0** represents the absence (e.g., a black pixel, an inactive node).  

When working with continuous data (e.g., values between 0.0 and 1.0), we can apply a **threshold** (`threshold`) to decide from which value we consider an element to be “active” and part of a cluster.

This package implements a **connected components search algorithm** (similar to Depth-first Search (DFS) in graphs), extended to work in **2D and 3D**.

---

## Applications

This algorithm was originally developed as a method to identify signals produced by **minimum ionizing particles (such as muons)** passing through a prototype hadronic calorimeter of size **1 m³**, based on gaseous detectors with copper pads of 1 cm² for signal collection.  

The signals produced by the passage of particles are recorded with a **semi-digital readout (SDHCAL – SemiDigital Hadronic Calorimeter)**.

---

## Features

- Cluster detection in **2D and 3D**.  
- Support for **binary and continuous matrices**.  
- Configurable threshold (`threshold`) to define which values are considered active.  
- Option to count only **orthogonal connections** or include **diagonals**.  
- Support for defining a minimum cluster size (`min_size`).  

---

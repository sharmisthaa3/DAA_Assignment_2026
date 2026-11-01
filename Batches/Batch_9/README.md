# Batch 9 — Large-Number Multiplication for HSM

**Course:** 23I501 Design and Analysis of Algorithms, PSG College of Technology

**Project topic:** Large-number multiplication for HSM  
**Chosen technique:** Divide and Conquer — Karatsuba multiplication  
**Rejected alternative:** Conventional schoolbook multiplication

## Members

- **Abhinandhana** — 24I301 — GitHub: `abhinandanar25`
- **Guruvarshana** — 24I317 — GitHub: `Guruvarshnaa-Vasanthakumar`
- **Nivarthna** — 24I334 — GitHub: `Nivarthna`
- **Pravesha** — 24I342 — GitHub: `Pravesha06`
- **Sharmisthaa** — 24I376 — GitHub: `sharmisthaa3`

**Presentation video:**  
https://drive.google.com/file/d/1FsxJFgREwdcexenaXr_8WA6CK4jb_WHC/view?usp=sharing

> Ensure the video is shared with **Anyone with the link can view** access before submission.

## 0. Contribution table

| Member | Files assigned / contributed | Main responsibility |
|---|---|---|
| Sharmisthaa (24I376, `sharmisthaa3`) | `code/main_solution.py`, `code/RUN.md`, `README.md` | Karatsuba implementation, run instructions, and report integration |
| Abhinandhana (24I301, `abhinandhanar25`) | `code/generate_inputs.py`, `contributions/24i301_Abhinandhana_complexity_worst_case.md` | Input generation and complexity / worst-case analysis |
| Guruvarshana (24I317, `Guruvarshanaa-Vasanthakumar`) | `code/rejected_alternative.py`, `contributions/24i317_Guruvarshana_algorithm_trace_proof.md` | Rejected alternative and algorithm trace / correctness discussion |
| Nivarthna (24I334, `Nivarthna`) | `slides.pdf`, `slides.pptx`, `contributions/24i334_Nivarthna_problem_model_data_structures.md` | Problem modelling, data representation, and presentation materials |
| Pravesha (24I344, `Pravesha06`) | `code/benchmark.py`, `results/timing.csv`, `results/timing_plot.png`, `contributions/24i044_Pravesha_implementation_results.md` | Benchmarking and experimental results |

Each member should commit their own contribution using their own GitHub account. The table should reflect the work actually completed by each member.

## 1. Problem modelling

The task is to multiply two large non-negative integers, `x` and `y`, and return the exact product `x × y`.

- **Input:** Two large integers.
- **Output:** Their exact product.
- **Correctness requirement:** The returned result must equal ordinary integer multiplication for every supported input.
- **Design goal:** Study whether a Divide and Conquer algorithm can reduce the number of recursive multiplications compared with the conventional schoolbook method.

For very large values, the number of digits is a useful measure of input size. Let `n` denote the number of digits (or, equivalently for asymptotic analysis, the input size up to a constant-factor representation choice).

## 2. Design technique: Divide and Conquer

Karatsuba multiplication is a Divide and Conquer algorithm. It splits each number into high and low parts, recursively multiplies smaller values, and combines the partial results.

Write the two inputs in base `B` as:

- `x = a × B^m + b`
- `y = c × B^m + d`

Then:

- `z₂ = a × c`
- `z₀ = b × d`
- `z₁ = (a + b) × (c + d) − z₂ − z₀`

The product is:

`x × y = z₂ × B^(2m) + z₁ × B^m + z₀`

The key idea is that Karatsuba computes the cross term using one additional recursive multiplication, `(a+b)(c+d)`, rather than computing both `ad` and `bc` separately. This reduces the recurrence from four recursive multiplications to three.

## 3. Algorithm outline

1. If either input is small enough for the base case, multiply directly.
2. Determine the split position based on the input lengths.
3. Split each input into high and low parts.
4. Recursively compute `z₂ = a × c`.
5. Recursively compute `z₀ = b × d`.
6. Recursively compute `z₁ = (a+b) × (c+d) − z₂ − z₀`.
7. Combine the partial results using the appropriate powers of the base.
8. Return the exact product.

See `code/main_solution.py` for the implementation and `code/RUN.md` for execution instructions.

## 4. Rejected alternative: schoolbook multiplication

Schoolbook multiplication is the conventional digit-by-digit method. Each digit of one number is multiplied by each digit of the other number, and the partial products are added with place-value shifts.

For two `n`-digit inputs, this method performs Θ(n²) single-digit multiplication work in the standard digit-based model. It is straightforward and often effective for small inputs, but its asymptotic growth is slower than Karatsuba's for sufficiently large inputs.

Schoolbook multiplication remains a useful base case for recursive multiplication because recursion has overhead and direct multiplication can be faster for small values. The project compares it as the alternative technique; the crossover point depends on the implementation and test environment.

## 5. Complexity analysis

### Karatsuba multiplication

Karatsuba makes three recursive multiplications on inputs of roughly half the original size. The remaining work consists of splitting, additions, subtractions, and recombination.

The recurrence is:

`T(n) = 3T(n/2) + O(n)`

By the Master Theorem:

`T(n) = Θ(n^(log₂ 3)) ≈ Θ(n^1.585)`

This is asymptotically faster than Θ(n²) schoolbook multiplication for sufficiently large inputs.

### Schoolbook multiplication

The conventional method multiplies every digit of one input by every digit of the other:

`T(n) = Θ(n²)`

### Practical considerations

- Karatsuba has extra recursion and intermediate arithmetic overhead.
- Schoolbook multiplication can be faster for small operands.
- The practical crossover depends on the language, implementation, hardware, and base-case threshold.
- Worst-case asymptotic analysis and measured running time describe different things; timing results must be reported from the actual experiment.

See the individual contribution notes for additional analysis.

## 6. Data representation

The implementation should use a representation that preserves the exact integer values and supports splitting and recombination. In Python, integers have arbitrary precision, so the implementation can work directly with integer values while using the number of digits to determine the split.

When describing results, identify the input-size measure used by the benchmark (for example, number of decimal digits). Keep the input generation, measurement, and plotting procedures consistent.

## 7. Implementation and repository contents

The Batch 9 folder contains the following project files:

- `README.md` — project report and repository guide.
- `slides.pdf` — presentation slides in PDF format.
- `slides.pptx` — editable presentation file.
- `analysis_sheet.pdf` — assignment analysis sheet.
- `code/main_solution.py` — chosen Karatsuba implementation.
- `code/rejected_alternative.py` — implementation of the rejected alternative.
- `code/generate_inputs.py` — input generator for experiments.
- `code/benchmark.py` — timing and comparison script.
- `code/RUN.md` — instructions for running the code.
- `results/timing.csv` — recorded timing data.
- `results/timing_plot.png` — plot generated from the timing data.
- `results/README.txt` — notes about the results.
- `contributions/` — individual member contribution notes.
- `CONTRIBUTIONS_AND_PR_TEMPLATE.txt` — contribution and pull-request guidance.

## 8. Experimental methodology and results

The benchmarking script and recorded data are in `code/benchmark.py` and `results/timing.csv`. The plot is in `results/timing_plot.png`.

For a fair comparison:

1. Generate reproducible inputs at several increasing digit lengths.
2. Check that both implementations return the same product before recording timings.
3. Run both methods under the same environment and input conditions.
4. Repeat measurements where practical and use a consistent summary statistic.
5. Plot input size against measured execution time.
6. Report the machine, Python version, input-size definition, and any relevant implementation threshold if available.

Use the values in `results/timing.csv` as the source of reported measurements. Do not describe theoretical estimates as measured results, and do not claim measurements from a different language or hardware unless those experiments were actually performed.

## 9. How to run

From the `Batch_9` directory, follow the commands and prerequisites documented in `code/RUN.md`.

The main files are:

- Chosen method: `code/main_solution.py`
- Alternative method: `code/rejected_alternative.py`
- Input generation: `code/generate_inputs.py`
- Benchmarking: `code/benchmark.py`

If a command fails, check that Python is installed and that the command is being run from the correct directory. Preserve the input settings used to create the results so the experiment can be repeated.

## 10. Correctness argument

Karatsuba follows directly from algebraic expansion.

Given:

`x = aB^m + b` and `y = cB^m + d`,

their product is:

`xy = acB^(2m) + (ad + bc)B^m + bd`.

Since:

`(a+b)(c+d) = ac + ad + bc + bd`,

we obtain:

`ad + bc = (a+b)(c+d) − ac − bd`.

Substituting `z₂ = ac`, `z₀ = bd`, and `z₁ = (a+b)(c+d) − z₂ − z₀` gives:

`xy = z₂B^(2m) + z₁B^m + z₀`.

Thus, if each recursive multiplication returns the correct product and the base case is correct, the combination step returns the correct product. By induction on the input size, the algorithm is correct.

## 11. Presentation

**Presentation video:**  
https://drive.google.com/file/d/1FsxJFgREwdcexenaXr_8WA6CK4jb_WHC/view?usp=sharing

The presentation should cover:

1. Problem statement and input/output model.
2. Why large-number multiplication is relevant to HSM.
3. Divide and Conquer and the Karatsuba formula.
4. A worked example or trace.
5. Complexity analysis and comparison with schoolbook multiplication.
6. Implementation and correctness.
7. Experimental methodology, timing plot, and limitations.
8. Conclusion and each member's contribution.

All five members should present their assigned parts in the video. Keep the video within the instructor's time limit and ensure that anyone with the link can view it.

## 12. Conclusion

This project studies large-number multiplication using Karatsuba's Divide and Conquer technique. By reducing the recursive multiplications from four to three, Karatsuba achieves the recurrence `T(n) = 3T(n/2) + O(n)` and asymptotic time complexity Θ(n^1.585). This improves on the Θ(n²) complexity of conventional schoolbook multiplication for sufficiently large inputs.

The timing data and plot in `results/` should be used to discuss observed performance on the tested inputs. Actual performance depends on input size, implementation overhead, and the execution environment.

## References

1. Course materials for 23I501 — Design and Analysis of Algorithms.
2. Assignment instructions and report template provided by the course instructor.
3. Karatsuba, A. and Ofman, Yu. (1962). *Multiplication of Many-Digital Numbers by Automatic Computers*.
4. Python documentation: https://docs.python.org/3/

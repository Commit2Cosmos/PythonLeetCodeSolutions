mod n_queens;

use pyo3::prelude::*;


#[pymodule]
fn funcs_rs(_py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {

    // let child_mod = PyModule::new_bound(py, "n_queens")?;
    // child_mod.add_function(wrap_pyfunction!(n_queens::solve_n_queens, m)?)?;
    // m.add_submodule(&child_mod)?;

    m.add_function(wrap_pyfunction!(n_queens::solve_n_queens, m)?)?;

    Ok(())
}
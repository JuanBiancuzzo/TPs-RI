# /// script
# dependencies = [
#     "marimo>=0.23.3",
#     "marimo-studio[deno]==0.2.3"
# ]
# requires-python = ">=3.14,<3.15"
#
# [tool.marimo-studio]
# default = "presentacion"
#
# [tool.marimo-studio.cells]
# cell-2 = {ref = "cell:v1:d08e3a9902507e2688643e7b944a85f684716a4d07ed1ca111d2aa70f54f3843:d08e3a9902507e2688643e7b944a85f684716a4d07ed1ca111d2aa70f54f3843:0"}
# cell-3 = {ref = "cell:v1:c78c7a5ba05e4c000765722439a5734d1b0f6a985111d9461880cc375e816784:c78c7a5ba05e4c000765722439a5734d1b0f6a985111d9461880cc375e816784:0"}
# ///

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(0, 5, 0.1)
    slider
    return (slider,)


@app.cell
def _(slider):
    print(f"El valor del slider es: {slider.value}")
    return


if __name__ == "__main__":
    app.run()

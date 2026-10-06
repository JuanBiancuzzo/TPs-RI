import { Slide } from "@revealjs/react";

export const Introduccion = () => {
    return (<>
        <Slide key="cell-2">
          <h2> Mira tengo un slider </h2>
          <marimo-cell name="cell-2" />
        </Slide>
        <Slide key="cell-3">
          <h2> Uso el valor del slider </h2>
          <marimo-cell name="cell-3" />
        </Slide>
    </>);
}

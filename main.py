from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import typer
from bs4 import BeautifulSoup, Tag

app = typer.Typer()


@dataclass
class AnimationParameters:
    duration: str = "0.5s"
    repeat_count: str = "1"
    begin: str = "0s"
    fill: str = "freeze"
    keySplines: str = ""
    calcMode: str = "linear"

    def as_animate_attrs(self):
        attrs = {
            "begin": self.begin,
            "repeatCount": self.repeat_count,
            "dur": self.duration,
            "fill": self.fill,
            "calcMode": self.calcMode,
        }
        if self.calcMode == "spline":
            attrs["keySplines"] = self.keySplines
        return attrs


def create_anim_element(
    soup: BeautifulSoup,
    values: str,
    params: AnimationParameters,
) -> Tag:
    element = soup.new_tag(
        "animate",
        attrs={
            "attributeName": "d",
            "values": values,
        },
    )
    element.attrs.update(params.as_animate_attrs())
    return element


def add_path_animation(
    soup_s: BeautifulSoup,
    elem_start: Tag,
    elem_target: Tag,
    params: AnimationParameters,
) -> None:
    path_s = elem_start.attrs["d"]
    path_e = elem_target.attrs["d"]

    values = ";".join([path_s, path_e])
    anim_element = create_anim_element(soup_s, values, params)
    elem_start.append(anim_element)


def animate(
    start: str,
    target: str,
    output: str,
    params: AnimationParameters,
) -> None:
    tree_start = BeautifulSoup(Path(start).read_text(), "xml")
    tree_target = BeautifulSoup(Path(target).read_text(), "xml")

    for elem_s in tree_start.find_all("path"):
        for elem_e in tree_target.find_all("path"):
            if elem_s.attrs["id"] == elem_e.attrs["id"]:
                add_path_animation(tree_start, elem_s, elem_e, params)
                break

    Path(output).write_text(str(tree_start))


@app.command("linear")
def morph_linear(
    start: str,
    target: str,
    output: Optional[str] = "animated.svg",
    duration: Optional[str] = AnimationParameters.duration,
    repeat_count: Optional[str] = AnimationParameters.repeat_count,
    begin: Optional[str] = AnimationParameters.begin,
    fill_mode: Optional[str] = AnimationParameters.fill,
):
    parameters = AnimationParameters(
        duration=duration,
        repeat_count=repeat_count,
        begin=begin,
        fill=fill_mode,
    )
    animate(start, target, output, parameters)


@app.command("spline")
def morph_spline(
    start: str,
    target: str,
    output: Optional[str] = "animated.svg",
    duration: Optional[str] = AnimationParameters.duration,
    repeat_count: Optional[str] = AnimationParameters.repeat_count,
    begin: Optional[str] = AnimationParameters.begin,
    fill_mode: Optional[str] = AnimationParameters.fill,
    keySplines: Optional[str] = "1 0 .5 .5",
):
    parameters = AnimationParameters(
        duration=duration,
        repeat_count=repeat_count,
        begin=begin,
        fill=fill_mode,
        keySplines=keySplines,
        calcMode="spline",
    )
    animate(start, target, output, parameters)


if __name__ == "__main__":
    app()

from pathlib import Path

def save_plot(plt_obj, path: str) -> str:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    plt_obj.tight_layout()
    plt_obj.savefig(path, dpi=150, bbox_inches="tight")
    
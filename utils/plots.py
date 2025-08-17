from pathlib import Path

def save_plot(plt_obj, save_path):
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    plt_obj.tight_layout()
    plt_obj.savefig(save_path, dpi=150, bbox_inches="tight")
    plt_obj.close()
    return str(save_path)
from typing import Callable, Optional, Dict, Any
from fastapi import Request
import pandas as pd
from utils.templates import templates
from utils.common_metrics import get_metrics
from utils.report_texts import get_notes

def render_simple_report(
    request: Request,
    title: str,
    get_df: Callable[[], "pd.DataFrame"],
    compute: Callable[[Any], Any],
    chart: Optional[Callable[[Any, str], None]] = None,
    image_name: Optional[str] = None,
    template_name: str = "report.html",
    analysis_key = None,
    result_preview_rows: int = 10,
    show_footer = True,
    footer_left: Optional[str] = None,
    footer_right: Optional[str] = None,
):
    df = get_df()
    result = compute(df)
    image_path = None
    if chart and image_name:
        image_path = f"static/images/{image_name}"
        chart(result, image_path)
    result_preview_html = None
    try:
        import pandas as pd 
        if hasattr(result, "head") and hasattr(result, "to_html"):
            result_preview_html = (
                result.head(result_preview_rows)
                      .to_html(classes="table table-striped table-sm", index=False)
            )
    except Exception:
        pass

    if footer_left is None:
        last_dt = getattr(df["InvoiceDate"].max(), "date", lambda: None)()
        footer_left = f"Источник: Online Retail · Обновлено: {last_dt or ''}".strip()

    if footer_right is None:
        footer_right = '<a href="/" class="btn btn-sm btn-outline-secondary">На главную</a>'

    context = {
        "request": request,
        "title": title,
        "total_customers": int(getattr(df["CustomerID"], "nunique", lambda: None)() or 0),
        "image_url": f"/{image_path}" if image_path else None,
        "metrics": get_metrics(analysis_key),
        "notes": get_notes(analysis_key),
        "result_preview_html": result_preview_html,
        "show_footer": show_footer,
        "footer_right": footer_right,
        "footer_left": footer_left
    }
    return templates.TemplateResponse(template_name, context)
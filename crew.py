import os
from crewai import Crew, Process

from agents import (
    build_parser_agent, build_ats_writer_agent,
    build_evaluator_agent, build_refiner_agent
)
from tasks import (
    parse_resume_task, rewrite_for_ats_task,
    evaluate_ats_task, refine_bullets_task
)


def run_pipeline(raw_resume_text: str, job_title: str, job_description: str):
    """Run the full 4-agent ATS optimization pipeline.
    
    Args:
        raw_resume_text: Raw text extracted from the uploaded resume PDF
        job_title: Target job title
        job_description: Full job description to optimize against
        
    Returns:
        tuple: (cleaned_resume, rewritten_resume, refined_resume, evaluation)
    """
    # Build agents
    parser = build_parser_agent()
    writer = build_ats_writer_agent()
    refiner = build_refiner_agent()
    evaluator = build_evaluator_agent()

    # Stage 1: Parse and clean resume
    t_parse = parse_resume_task(parser, raw_resume_text)
    parse_crew = Crew(agents=[parser], tasks=[t_parse], process=Process.sequential, verbose=True)
    parse_result = parse_crew.kickoff()
    cleaned = str(parse_result).strip()

    # Stage 2: Rewrite for ATS alignment with job description
    t_rewrite = rewrite_for_ats_task(writer, cleaned, job_title, job_description)
    rewrite_crew = Crew(agents=[writer], tasks=[t_rewrite], process=Process.sequential, verbose=True)
    rewrite_result = rewrite_crew.kickoff()
    rewritten = str(rewrite_result).strip()

    # Stage 3: Refine bullet points for impact and clarity
    t_refine = refine_bullets_task(refiner, rewritten)
    refine_crew = Crew(agents=[refiner], tasks=[t_refine], process=Process.sequential, verbose=True)
    refine_result = refine_crew.kickoff()
    final_resume = str(refine_result).strip()

    # Stage 4: Score and evaluate ATS match quality
    t_eval = evaluate_ats_task(evaluator, final_resume, job_title, job_description)
    eval_crew = Crew(agents=[evaluator], tasks=[t_eval], process=Process.sequential, verbose=True)
    eval_result = eval_crew.kickoff()
    evaluation = str(eval_result).strip()

    return cleaned, rewritten, final_resume, evaluation


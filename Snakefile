rule run_workflow:
    input:
        "{file}.xlsx",
    output:
        "{file}_result.xlsx",
    log:
        "{file}.log",
    conda:
        "envs/workflow_env.yaml"
    script:
        "workflow.py"

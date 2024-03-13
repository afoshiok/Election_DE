CREATE TABLE IF NOT EXISTS src_operating_expenditures (
    cmte_id varchar(9),
    amndt_ind varchar(1),
    rpt_yr number(4),
    rpt_tp varchar(3),
    image_num varchar(18),
    line_num varchar(30),
    form_tp_cd varchar(8),
    sched_tp_cd varchar(8),
    name varchar(200),
    city varchar(30),
    state varchar(2),
    zip_code varchar(9),
    transaction_dt date,
    transaction_amt number(14,2),
    transaction_pgi varchar(5),
    purpose varchar(100),
    category varchar(3),
    category_desc varchar(40),
    memo_cd varchar(1),
    memo_text varchar(100),
    entity_tp varchar(3),
    sub_id number(19),
    file_num number(7),
    tran_id varchar(32),
    back_ref_tran_id varchar(32)
)
CREATE TABLE IF NOT EXISTS individual_contributions (
    sub_id varchar(9),
    cmte_id varchar(9),
    amndt_id varchar(1),
    rpt_tp varchar(3),
    transaction_pgi varchar(5),
    image_num varchar(18),
    transaction_tp varchar(3),
    entity_tp varchar(3),
    name varchar(200),
    city varchar(30),
    state varchar(2),
    zip_code varchar(9),
    occupation varchar(38),
    transaction_dt date,
    transaction_amt number(14,2),
    other_id varchar(9),
    tran_id varchar(32),
    file_num number(22),
    memo_cd varchar(1),
    memo_text varchar(100)
)
streamlit.errors.StreamlitDuplicateElementKey: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:
File "/mount/src/test/streamlit_app.py", line 84, in <module>
    if st.button("回答する", key=f"answer_btn_{st.session_state.current_question}"):
       ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/metrics_util.py", line 443, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/elements/widgets/button.py", line 268, in button
    return self.dg._button(
           ~~~~~~~~~~~~~~~^
        label,
        ^^^^^^
    ...<10 lines>...
        width=width,
        ^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/elements/widgets/button.py", line 1121, in _button
    element_id = compute_and_register_element_id(
        "button",
    ...<7 lines>...
        width=width,
    )
File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/elements/lib/utils.py", line 253, in compute_and_register_element_id
    _register_element_id(ctx, element_type, element_id)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/elements/lib/utils.py", line 145, in _register_element_id
    raise StreamlitDuplicateElementKey(user_key)
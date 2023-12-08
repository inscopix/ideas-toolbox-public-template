TOOL_OUTPUT_FILE="../ideas-toolbox-my-toolbox/outputs/example_tool__test_func_1/tool_output.txt"
if test -f "$TOOL_OUTPUT_FILE"; then
    echo "✅ Tool has successfully run in docker"
else 
    echo "❌ Tool run failure"
    exit 1
fi
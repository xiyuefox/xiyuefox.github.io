#!/bin/bash
# Bilingual Content Update Template

# For each activity section, use this format:
# <div class="activity content-en">
#   <h4>English Activity Title</h4>
#   ... English content ...
# </div>

# <div class="activity content-zh">
#   <h4>Chinese Activity Title</h4>
#   ... Chinese content ...  
# </div>

# Example:
echo "<div class='activity content-en'>"
echo "    <h4>1. 'Narrate Your Day'</h4>"
echo "    <p><strong>What:</strong> Talk through everything you do</p>"
echo "    <p><strong>Why it matters:</strong> Babies learn language by hearing 21,000 words/day</p>"
echo "    <p><strong>How:</strong> 'Now I'm changing your diaper. Here's the clean one. It's soft and white.'</p>"
echo "    <div class='parent-tip'>"
echo "        <strong>Parent tip:</strong> Feel silly? Your baby is absorbing every word."
echo "    </div>"
echo "</div>"

echo ""

echo "<div class='activity content-zh'>"
echo "    <h4>1. '讲述你的一天'</h4>"
echo "    <p><strong>内容:</strong> 讲述你做的每一件事</p>"
echo "    <p><strong>重要性:</strong> 婴儿通过每天听到21,000个单词来学习语言</p>"
echo "    <p><strong>做法:</strong> '现在我正在给你换尿布。这是干净的。它又软又白。'</p>"
echo "    <div class='parent-tip'>"
echo "        <strong>家长提示:</strong> 觉得傻吗？你的宝宝正在吸收每一个单词。"
echo "    </div>"
echo "</div>"

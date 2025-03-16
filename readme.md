# 🚀 LLM Engineering: Mastering Generative AI & Language Models

> Repository documenting my learning journey through the "LLM Engineering: Master AI, Large Language Models & Agents" course.

## 📋 Course Overview

This comprehensive 8-week program focuses on building practical AI applications using both frontier and open-source language models. Led by industry veteran Ed Donner, the course provides hands-on experience with cutting-edge AI technologies through real-world projects.

## 🛠️ Key Technologies Explored

- **Frontier Models**: Claude, GPT-4, Gemini
- **Open-Source Models**: Llama 3.1, Phi-3, Qwen2, Starcoder2
- **Frameworks**: LangChain, HuggingFace Transformers, Gradio
- **Techniques**: RAG, QLoRA fine-tuning, Agents, Multi-modal processing

## 🧠 What I've Learned So Far

### Week 1-2: Foundations & Frontier APIs
- Transformer architecture fundamentals
- Building web-scraping AI solutions
- Customer service chatbot development

### Week 3: Open-Source Model Exploration
- **Tokenizer Implementation & Comparison**: Analyzed efficiency differences between Phi-3, Qwen2, and Starcoder2 tokenizers
- Working with HuggingFace ecosystem
- Building audio-to-text meeting minutes generator

## 🔍 Featured Project: Multi-Model Meeting Minutes Generator

Implemented a system that:
1. Takes meeting audio recordings from Google Drive
2. Transcribes speech using Whisper API
3. Generates structured meeting minutes with Llama 3.1
4. Produces markdown-formatted output with:
   - Meeting summary
   - Key discussion points
   - Action items with owners
   - Next steps

```python
# Sample code for tokenizer comparison
text = "I am excited to show Tokenizers in action to my LLM engineers"

# Compare token efficiency across models
phi3_tokens = phi3_tokenizer.encode(text)    # 15 tokens
qwen2_tokens = qwen2_tokenizer.encode(text)  # 14 tokens
llama_tokens = tokenizer.encode(text)        # 15 tokens
```

## 💡 Key Insights

- **Token Efficiency Matters**: Qwen2's tokenizer consistently produces more compact representations, which translates to cost savings in production
- **Chat Templates**: Each model requires specific formatting patterns for optimal results
- **Specialized Models**: Starcoder2 excels at code tokenization, showing the importance of model selection for specific use cases

## 🔭 Upcoming Topics

- LLM selection strategies for business applications
- RAG implementation for enhanced accuracy
- Fine-tuning techniques for specialized tasks
- Multi-agent systems development

## 📈 Skills Developed

- Selecting appropriate models for specific tasks
- Implementing and optimizing tokenizers
- Building end-to-end AI applications
- Comparative performance analysis of open-source vs. frontier models

---

*This repository serves as my learning journal as I develop expertise in LLM engineering and generative AI applications. Code samples and project implementations will be updated throughout the course.*
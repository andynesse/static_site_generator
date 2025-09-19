[< Back Home](/)

# How to Generate Your Own Lorem Ipsum Variants

**Posted on:** March 12, 2024
**Author:** Code Enthusiast

![Code screenshot](/images/code-screen.jpg)

While standard Lorem Ipsum is useful, sometimes you need specialized placeholder text for different contexts and industries.

> "Custom placeholder text can better communicate the intent of design elements."
>
> — Design Systems Weekly

## Standard Lorem Ipsum Generators

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.

Popular generators include:
- LoremIpsum.io
- Lipsum.com
- UI Placeholder

## Industry-Specific Variants

Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Different industries have developed their own flavor of placeholder text:

### For Different Industries:
- **Cupcake Ipsum** - For food blogs and restaurants
- **Hipster Ipsum** - For trendy startups and agencies
- **Corporate Ipsum** - For business and finance sites
- **Cat Ipsum** - For pet-related businesses

## Creating Your Own Generator

Here's a simple JavaScript function to create custom placeholder text:

```javascript
function customIpsum(vocabulary, paragraphs) {
  let output = '';
  for (let p = 0; p < paragraphs; p++) {
    let sentence = '';
    for (let w = 0; w < 15; w++) {
      sentence += vocabulary[Math.floor(Math.random() * vocabulary.length)] + ' ';
    }
    output += '<p>' + sentence.trim() + '.</p>';
  }
  return output;
}

// Usage with tech terms
const techWords = ['API', 'framework', 'database', 'cloud', 'responsive'];
console.log(customIpsum(techWords, 2));
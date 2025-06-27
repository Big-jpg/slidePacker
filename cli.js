// cli.js
import 'dotenv/config';
import FirecrawlApp from '@mendable/firecrawl-js';
import { generateSlides } from './generate-slideshow.js';
import { Command } from 'commander';

const program = new Command();
program
  .option('--query <string>', 'Search query', 'AI trends 2025')
  .parse(process.argv);

const options = program.opts();
const query = options.query;

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

console.log(`🔍 Searching for: "${query}"...`);
const searchResults = await firecrawl.search(query, {
  limit: 5,
  scrapeOptions: {
    formats: ['markdown']
  }
});

await generateSlides(searchResults.data, query);

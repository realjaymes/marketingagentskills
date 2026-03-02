/**
 * Skill to Prompt - DOCX Generator
 *
 * Generates Word documents for ChatGPT Project conversion:
 * - 1 prompt instruction document (.docx)
 * - 1-3 knowledge file documents (.docx)
 *
 * Usage:
 *   node docx-generator.js <conversion-data.json>
 *
 * Prerequisites:
 *   npm install docx
 *   Package available at ~/Documents/node_modules/docx
 *
 * Input JSON structure:
 * {
 *   "skillName": "Copywriting",
 *   "originalSkillName": "copywriting",
 *   "version": "1.0.0",
 *   "outputDir": "./",
 *   "instructionDoc": {
 *     "filename": "Copywriting_Prompt_Instructions.docx",
 *     "title": "Copywriting — ChatGPT Project Instructions",
 *     "characterCount": 6842,
 *     "sections": [
 *       { "type": "heading", "level": 1, "text": "Role" },
 *       { "type": "paragraph", "text": "You are..." },
 *       { "type": "bullet", "text": "First point", "level": 0 },
 *       { "type": "numbered", "text": "Step one", "number": 1 },
 *       { "type": "bold-paragraph", "label": "Goal:", "text": "To produce..." },
 *       { "type": "table", "headers": ["Col1", "Col2"], "rows": [["a","b"]], "columnPcts": [30, 70] },
 *       { "type": "divider" },
 *       { "type": "page-break" }
 *     ]
 *   },
 *   "knowledgeFiles": [
 *     {
 *       "filename": "Copywriting_Reference_Guide.docx",
 *       "title": "Copywriting Reference Guide",
 *       "sections": [...]
 *     }
 *   ]
 * }
 */

const {
  Document,
  Packer,
  Paragraph,
  Table,
  TableRow,
  TableCell,
  TextRun,
  HeadingLevel,
  AlignmentType,
  WidthType,
  ShadingType,
  PageBreak,
  TableLayoutType,
  BorderStyle,
  convertInchesToTwip,
} = require("docx");
const fs = require("fs");
const path = require("path");

// Formatting constants matching James's standards
const FONT = "Arial";
const SIZES = {
  normal: 20, // 10pt = 20 half-points
  small: 18, // 9pt
  h1: 40, // 20pt
  h2: 32, // 16pt
  h3: 28, // 14pt
  h4: 24, // 12pt
};
const LINE_SPACING = 276; // 1.15 in docx units (240 * 1.15)

// Page dimensions — Letter: 8.5" wide, margins 0.8" each side
const PAGE_MARGIN_TWIPS = convertInchesToTwip(0.8);
const PAGE_USABLE_WIDTH_TWIPS = convertInchesToTwip(6.9);

const COLORS = {
  text: "202124",
  textLight: "5f6368",
  white: "ffffff",
  headerBg: "e8e8e8",
  border: "cccccc",
  altRow: "f9f9f9",
  accent: "1a73e8",
  metaBg: "f0f4f9",
};

const BORDER_STYLE = {
  style: BorderStyle.SINGLE,
  size: 1,
  color: COLORS.border,
};

const CELL_MARGINS = {
  marginUnitType: WidthType.DXA,
  top: convertInchesToTwip(0.05),
  bottom: convertInchesToTwip(0.05),
  left: convertInchesToTwip(0.08),
  right: convertInchesToTwip(0.08),
};

/**
 * Convert percentage column widths to twip values.
 */
function percentToTwips(percentages) {
  return percentages.map((pct) =>
    Math.round((pct / 100) * PAGE_USABLE_WIDTH_TWIPS)
  );
}

// --- Helper functions ---

function createHeading(text, level) {
  const sizeMap = {
    1: SIZES.h1,
    2: SIZES.h2,
    3: SIZES.h3,
    4: SIZES.h4,
  };
  const headingMap = {
    1: HeadingLevel.HEADING_1,
    2: HeadingLevel.HEADING_2,
    3: HeadingLevel.HEADING_3,
    4: HeadingLevel.HEADING_4,
  };
  return new Paragraph({
    children: [
      new TextRun({
        text: text,
        font: FONT,
        size: sizeMap[level] || SIZES.h2,
      }),
    ],
    heading: headingMap[level] || HeadingLevel.HEADING_2,
    spacing: { before: 300, after: 150, line: LINE_SPACING },
  });
}

function createParagraph(text, options = {}) {
  return new Paragraph({
    children: [
      new TextRun({
        text: text,
        font: FONT,
        size: options.size || SIZES.normal,
        bold: options.bold || false,
        italics: options.italics || false,
        color: options.color || COLORS.text,
      }),
    ],
    spacing: { after: options.afterSpacing || 120, line: LINE_SPACING },
  });
}

function createBoldLabelParagraph(label, text) {
  return new Paragraph({
    children: [
      new TextRun({
        text: label + " ",
        font: FONT,
        size: SIZES.normal,
        bold: true,
        color: COLORS.text,
      }),
      new TextRun({
        text: text,
        font: FONT,
        size: SIZES.normal,
        color: COLORS.text,
      }),
    ],
    spacing: { after: 120, line: LINE_SPACING },
  });
}

function createBullet(text, level = 0) {
  return new Paragraph({
    children: [
      new TextRun({
        text: text,
        font: FONT,
        size: SIZES.normal,
        color: COLORS.text,
      }),
    ],
    bullet: { level: level },
    spacing: { after: 80, line: LINE_SPACING },
  });
}

function createNumberedItem(text, number) {
  // Simulated numbered list using indentation and manual numbering
  return new Paragraph({
    children: [
      new TextRun({
        text: `${number}. `,
        font: FONT,
        size: SIZES.normal,
        bold: true,
        color: COLORS.text,
      }),
      new TextRun({
        text: text,
        font: FONT,
        size: SIZES.normal,
        color: COLORS.text,
      }),
    ],
    indent: { left: convertInchesToTwip(0.25) },
    spacing: { after: 80, line: LINE_SPACING },
  });
}

function createTable(headers, rows, columnPcts) {
  const colTwips = percentToTwips(columnPcts);
  const tableRows = [];

  // Header row
  tableRows.push(
    new TableRow({
      tableHeader: true,
      children: headers.map(
        (header, i) =>
          new TableCell({
            children: [
              new Paragraph({
                children: [
                  new TextRun({
                    text: header,
                    font: FONT,
                    size: SIZES.normal,
                    bold: true,
                    color: COLORS.text,
                  }),
                ],
                spacing: { after: 20, line: LINE_SPACING },
              }),
            ],
            width: { size: colTwips[i], type: WidthType.DXA },
            shading: { fill: COLORS.headerBg, type: ShadingType.CLEAR },
            margins: CELL_MARGINS,
            verticalAlign: "center",
          })
      ),
    })
  );

  // Data rows
  rows.forEach((row, rowIdx) => {
    tableRows.push(
      new TableRow({
        children: row.map(
          (cell, i) =>
            new TableCell({
              children: [
                new Paragraph({
                  children: [
                    new TextRun({
                      text: String(cell || ""),
                      font: FONT,
                      size: SIZES.normal,
                      color: COLORS.text,
                    }),
                  ],
                  spacing: { after: 20, line: LINE_SPACING },
                }),
              ],
              width: { size: colTwips[i], type: WidthType.DXA },
              margins: CELL_MARGINS,
              verticalAlign: "top",
              shading:
                rowIdx % 2 === 1
                  ? { fill: COLORS.altRow, type: ShadingType.CLEAR }
                  : undefined,
            })
        ),
      })
    );
  });

  return new Table({
    rows: tableRows,
    width: { size: PAGE_USABLE_WIDTH_TWIPS, type: WidthType.DXA },
    columnWidths: colTwips,
    layout: TableLayoutType.FIXED,
    borders: {
      top: BORDER_STYLE,
      bottom: BORDER_STYLE,
      left: BORDER_STYLE,
      right: BORDER_STYLE,
      insideHorizontal: BORDER_STYLE,
      insideVertical: BORDER_STYLE,
    },
  });
}

function createDivider() {
  return new Paragraph({
    children: [
      new TextRun({
        text: "─".repeat(60),
        font: FONT,
        size: SIZES.small,
        color: COLORS.border,
      }),
    ],
    spacing: { before: 200, after: 200, line: LINE_SPACING },
  });
}

// --- Section renderer ---

/**
 * Render an array of section elements into docx Paragraph/Table objects.
 */
function renderSections(sections) {
  const elements = [];

  for (const section of sections) {
    switch (section.type) {
      case "heading":
        elements.push(createHeading(section.text, section.level || 2));
        break;

      case "paragraph":
        elements.push(createParagraph(section.text));
        break;

      case "bold-paragraph":
        elements.push(createBoldLabelParagraph(section.label, section.text));
        break;

      case "bullet":
        elements.push(createBullet(section.text, section.level || 0));
        break;

      case "numbered":
        elements.push(createNumberedItem(section.text, section.number || 1));
        break;

      case "table":
        elements.push(
          createTable(
            section.headers,
            section.rows,
            section.columnPcts || section.headers.map(() => Math.floor(100 / section.headers.length))
          )
        );
        elements.push(new Paragraph({ text: "", spacing: { after: 150 } }));
        break;

      case "divider":
        elements.push(createDivider());
        break;

      case "page-break":
        elements.push(new Paragraph({ children: [new PageBreak()] }));
        break;

      case "spacer":
        elements.push(
          new Paragraph({ text: "", spacing: { after: section.size || 200 } })
        );
        break;

      case "meta":
        // Light-background metadata block
        elements.push(
          createParagraph(section.text, {
            size: SIZES.small,
            color: COLORS.textLight,
            italics: true,
          })
        );
        break;

      default:
        // Treat unknown types as plain paragraph
        if (section.text) {
          elements.push(createParagraph(section.text));
        }
        break;
    }
  }

  return elements;
}

// --- Document builders ---

/**
 * Build a single .docx document from a file definition.
 */
async function buildDocument(fileDef, metadata) {
  const children = [];

  // Title
  children.push(
    new Paragraph({
      children: [
        new TextRun({
          text: fileDef.title || metadata.skillName,
          font: FONT,
          size: SIZES.h1,
        }),
      ],
      spacing: { before: 400, after: 200, line: LINE_SPACING },
    })
  );

  // Subtitle with conversion metadata
  children.push(
    createParagraph(
      `Converted from Claude skill: ${metadata.originalSkillName} v${metadata.version}`,
      { size: SIZES.small, color: COLORS.textLight, italics: true }
    )
  );

  // Character count for instruction docs
  if (fileDef.characterCount) {
    children.push(
      createParagraph(
        `Instruction character count: ${fileDef.characterCount.toLocaleString()} / 8,000`,
        { size: SIZES.small, color: COLORS.textLight, italics: true }
      )
    );
  }

  children.push(
    new Paragraph({ text: "", spacing: { after: 200 } })
  );

  // Render all sections
  const rendered = renderSections(fileDef.sections);
  children.push(...rendered);

  const doc = new Document({
    creator: "Skill to Prompt Converter",
    title: fileDef.title || metadata.skillName,
    description: `ChatGPT Project file converted from Claude skill: ${metadata.originalSkillName}`,
    styles: {
      default: {
        document: {
          run: {
            font: FONT,
            size: SIZES.normal,
            color: COLORS.text,
          },
          paragraph: {
            spacing: { line: LINE_SPACING },
          },
        },
      },
    },
    sections: [
      {
        properties: {
          page: {
            margin: {
              top: PAGE_MARGIN_TWIPS,
              bottom: PAGE_MARGIN_TWIPS,
              left: PAGE_MARGIN_TWIPS,
              right: PAGE_MARGIN_TWIPS,
            },
          },
        },
        children: children,
      },
    ],
  });

  return Packer.toBuffer(doc);
}

// --- Main ---

async function main() {
  const args = process.argv.slice(2);

  if (args.length < 1) {
    console.log("Usage: node docx-generator.js <conversion-data.json>");
    console.log("");
    console.log("Generates all .docx files defined in the conversion data:");
    console.log("  - 1 prompt instruction document");
    console.log("  - 1-3 knowledge file documents");
    console.log("");
    console.log("Example:");
    console.log("  node docx-generator.js copywriting-conversion.json");
    process.exit(1);
  }

  const dataFile = args[0];

  if (!fs.existsSync(dataFile)) {
    console.error(`Error: Data file not found: ${dataFile}`);
    process.exit(1);
  }

  let data;
  try {
    data = JSON.parse(fs.readFileSync(dataFile, "utf-8"));
  } catch (err) {
    console.error(`Error parsing JSON: ${err.message}`);
    process.exit(1);
  }

  const outputDir = data.outputDir || ".";
  const metadata = {
    skillName: data.skillName,
    originalSkillName: data.originalSkillName,
    version: data.version || "1.0.0",
  };

  const generated = [];

  // Generate instruction document
  if (data.instructionDoc) {
    const buffer = await buildDocument(data.instructionDoc, metadata);
    const outputPath = path.join(outputDir, data.instructionDoc.filename);
    fs.writeFileSync(outputPath, buffer);
    generated.push(outputPath);
    console.log(`Instruction doc: ${outputPath}`);
  }

  // Generate knowledge files
  if (data.knowledgeFiles && data.knowledgeFiles.length > 0) {
    for (const kf of data.knowledgeFiles) {
      const buffer = await buildDocument(kf, metadata);
      const outputPath = path.join(outputDir, kf.filename);
      fs.writeFileSync(outputPath, buffer);
      generated.push(outputPath);
      console.log(`Knowledge file:  ${outputPath}`);
    }
  }

  console.log(`\nGenerated ${generated.length} file(s).`);
}

module.exports = { buildDocument, renderSections };

if (require.main === module) {
  main();
}

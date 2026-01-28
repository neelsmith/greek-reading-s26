function Div(el)
  if el.classes:includes("columns") and FORMAT:match("latex") then
    -- Extract column contents (skip spacer columns)
    local columns = {}
    for _, child in ipairs(el.content) do
      if child.t == "Div" and child.classes:includes("column") then
        -- Check if this is a content column (not a spacer)
        if #child.content > 0 then
          table.insert(columns, child.content)
        end
      end
    end
    
    -- Process if we found 2 content columns
    if #columns == 2 then
      local result = {}
      
      -- Start paracol environment
      table.insert(result, pandoc.RawBlock("latex", "\\begin{paracol}{2}"))
      
      -- First column content
      for _, block in ipairs(columns[1]) do
        table.insert(result, block)
      end
      
      -- Switch to second column
      table.insert(result, pandoc.RawBlock("latex", "\\switchcolumn"))
      
      -- Second column content
      for _, block in ipairs(columns[2]) do
        table.insert(result, block)
      end
      
      -- End paracol environment
      table.insert(result, pandoc.RawBlock("latex", "\\end{paracol}"))
      
      return result
    end
  end
  
  return el
end

-- Auto-generated idempotent SQL to add/refresh the '🏛️ Real Past Exams (2024–2025)' column
-- on the existing Digital SAT 1500+ Task Board WITHOUT modifying existing columns or progress.
BEGIN;
DO $$
DECLARE
  v_tpl_id uuid;
  v_col_id uuid;
  v_card_id uuid;
  v_next_order int;
BEGIN
  SELECT id INTO v_tpl_id FROM public.board_templates WHERE course_id = '871fdd8e-96a4-4e4b-92a2-2cd41021ee82' ORDER BY created_at ASC LIMIT 1;
  IF v_tpl_id IS NULL THEN
    RAISE EXCEPTION 'Digital SAT 1500+ board_template not found';
  END IF;

  -- Remove previous copy of this Real Past Exams column if re-running (idempotent)
  SELECT id INTO v_col_id FROM public.board_columns WHERE board_template_id = v_tpl_id AND title LIKE '%Real Past Exams%' LIMIT 1;
  IF v_col_id IS NOT NULL THEN
    DELETE FROM public.board_card_items WHERE card_id IN (SELECT id FROM public.board_cards WHERE column_id = v_col_id);
    DELETE FROM public.board_cards WHERE column_id = v_col_id;
    DELETE FROM public.board_columns WHERE id = v_col_id;
  END IF;

  SELECT COALESCE(MAX(order_index), 0) + 1 INTO v_next_order FROM public.board_columns WHERE board_template_id = v_tpl_id;
  INSERT INTO public.board_columns (course_id, board_template_id, title, order_index) VALUES ('871fdd8e-96a4-4e4b-92a2-2cd41021ee82', v_tpl_id, '🏛️ Real Past Exams (2024–2025 — 14 Đề Thi Thật) [color:#fef3c7,#b45309]', v_next_order) RETURNING id INTO v_col_id;
  INSERT INTO public.board_cards (column_id, title, order_index) VALUES (v_col_id, '1. Real Exams — Reading & Writing 2025 (7 Đề • 405 câu)', 1) RETURNING id INTO v_card_id;
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — May 2025 Reading & Writing (Full Adaptive • 81 Qs)', '', '7f7262bd-6587-4ee1-981c-42c9a23ad961', 1);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — June 2025 Ver 1 Reading & Writing (54 Qs)', '', 'd61ad4d1-0a2d-4a9a-98d4-6ff25bc706a6', 2);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — June 2025 US Ver 1 Reading & Writing (54 Qs)', '', 'c27be838-d4af-4df2-9815-80d8f6a38818', 3);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — March 2025 Ver 5 Reading & Writing (54 Qs)', '', 'a62db59d-efcb-41af-8118-4021148f8d83', 4);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — March 2025 Ver 3 Reading & Writing (54 Qs)', '', '6fe76b1f-7e6f-451b-bf00-76586991d6fd', 5);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — May 2025 Int. Ver 2 Reading & Writing (54 Qs)', '', '0e6c0285-80f4-49e4-b725-c7e12c2b430c', 6);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — May 2025 US Ver 4 Reading & Writing (54 Qs)', '', '514eae92-9f91-48f2-9c1a-b31d0bf87305', 7);
  INSERT INTO public.board_cards (column_id, title, order_index) VALUES (v_col_id, '2. Real Exams — Math 2024–2025 (7 Đề • 329 câu)', 2) RETURNING id INTO v_card_id;
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — SAT October Math (43 Qs • Official Key)', '', 'ea5a84ff-6d56-45b0-997b-b2293c97c8db', 1);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — May 2025 Math (Full Adaptive • 66 Qs)', '', '051f5176-66df-45d3-9741-f0380a4848e7', 2);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — June 2025 Ver 1 Math (Real M1 + M2)', '', '8b52c9f5-da2c-4f0a-a45c-f32f239dee4e', 3);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — June 2025 US Ver 1 Math (44 Qs)', '', 'cb318099-22a5-46c4-8e54-c1b9a112f0f2', 4);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — March 2025 Ver 5 Math (44 Qs)', '', 'fa00f947-bdfe-428c-818e-552f33993be5', 5);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — March 2025 Ver 3 Math (44 Qs)', '', '0eb57659-0c0e-44df-8d02-118d15a74de3', 6);
  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) VALUES (v_card_id, 'test', '🏛️ Real Exam — June 2025 Ver 2 Math (44 Qs)', '', 'b20b4095-f0cf-42d3-8bf2-6b1aa07be860', 7);
END $$;
COMMIT;
